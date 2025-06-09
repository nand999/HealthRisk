from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)

# --- Load Models and Preprocessors ---
# Ensure these paths are correct relative to app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVED_MODELS_DIR = os.path.join(BASE_DIR, 'saved_models')

# Diabetes Model
try:
    diabetes_model = tf.keras.models.load_model(os.path.join(SAVED_MODELS_DIR, 'diabetes_model'))
    diabetes_scaler = joblib.load(os.path.join(SAVED_MODELS_DIR, 'diabetes_scaler.pkl'))
    print("Diabetes model and scaler loaded.")
except Exception as e:
    print(f"Error loading Diabetes model/scaler: {e}")
    diabetes_model = None
    diabetes_scaler = None

# Hypertension Model
try:
    hypertension_model = tf.keras.models.load_model(os.path.join(SAVED_MODELS_DIR, 'hypertension_model'))
    hypertension_preprocessor = joblib.load(os.path.join(SAVED_MODELS_DIR, 'hypertension_preprocessor.pkl'))
    print("Hypertension model and preprocessor loaded.")
except Exception as e:
    print(f"Error loading Hypertension model/preprocessor: {e}")
    hypertension_model = None
    hypertension_preprocessor = None

# Stroke Model
try:
    stroke_model = tf.keras.models.load_model(os.path.join(SAVED_MODELS_DIR, 'stroke_model'))
    stroke_preprocessor = joblib.load(os.path.join(SAVED_MODELS_DIR, 'stroke_preprocessor.pkl'))
    print("Stroke model and preprocessor loaded.")
except Exception as e:
    print(f"Error loading Stroke model/preprocessor: {e}")
    stroke_model = None
    stroke_preprocessor = None

# --- Routes ---

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html')

@app.route('/predict_diabetes', methods=['GET', 'POST'])
def predict_diabetes():
    if request.method == 'POST':
        if not diabetes_model or not diabetes_scaler:
            return jsonify({'error': 'Diabetes model or scaler not loaded properly.'}), 500

        try:
            data = request.form.to_dict()
            # Convert values to float as expected by the model
            input_data = {
                'Age': float(data['Age']),
                'Sex': float(data['Sex']),
                'HighChol': float(data['HighChol']),
                'CholCheck': float(data['CholCheck']),
                'BMI': float(data['BMI']),
                'Smoker': float(data['Smoker']),
                'HeartDiseaseorAttack': float(data['HeartDiseaseorAttack']),
                'PhysActivity': float(data['PhysActivity']),
                'Fruits': float(data['Fruits']),
                'Veggies': float(data['Veggies']),
                'HvyAlcoholConsump': float(data['HvyAlcoholConsump']),
                'GenHlth': float(data['GenHlth']),
                'MentHlth': float(data['MentHlth']),
                'PhysHlth': float(data['PhysHlth']),
                'DiffWalk': float(data['DiffWalk']),
                'Stroke': float(data['Stroke']), # Note: This is confusing if stroke is also a prediction target elsewhere.
                                                 # Ensure consistency. Here, it's an input feature.
                'HighBP': float(data['HighBP'])
            }

            # Create a DataFrame in the exact order of training columns
            # Ensure the order matches the columns used during training
            feature_order = [
                'Age', 'Sex', 'HighChol', 'CholCheck', 'BMI', 'Smoker',
                'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
                'HvyAlcoholConsump', 'GenHlth', 'MentHlth', 'PhysHlth',
                'DiffWalk', 'Stroke', 'HighBP'
            ]
            
            # Convert input_data to a DataFrame for scaling
            input_df = pd.DataFrame([input_data], columns=feature_order)

            # Apply scaler to numerical columns
            numerical_cols_diabetes = ['Age', 'BMI', 'GenHlth', 'MentHlth', 'PhysHlth']
            input_df[numerical_cols_diabetes] = diabetes_scaler.transform(input_df[numerical_cols_diabetes])

            # Make prediction
            prediction_proba = diabetes_model.predict(input_df.values)[0][0]
            prediction_class = (prediction_proba > 0.5).astype(int)

            result = "Diabetes" if prediction_class == 1 else "No Diabetes"
            confidence = f"{prediction_proba * 100:.2f}%"

            return jsonify({'prediction': result, 'confidence': confidence})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return render_template('diabetes.html')

@app.route('/predict_hypertension', methods=['GET', 'POST'])
def predict_hypertension():
    if request.method == 'POST':
        if not hypertension_model or not hypertension_preprocessor:
            return jsonify({'error': 'Hypertension model or preprocessor not loaded properly.'}), 500

        try:
            data = request.form.to_dict()
            # Convert to appropriate types
            input_data = {
                'age': float(data['age']),
                'sex': float(data['sex']), # Assuming 0 or 1
                'cp': float(data['cp']),
                'trestbps': float(data['trestbps']),
                'chol': float(data['chol']),
                'fbs': float(data['fbs']), # Assuming 0 or 1
                'restecg': float(data['restecg']),
                'thalach': float(data['thalach']),
                'exang': float(data['exang']), # Assuming 0 or 1
                'oldpeak': float(data['oldpeak']),
                'slope': float(data['slope']),
                'ca': float(data['ca']),
                'thal': float(data['thal'])
            }

            # Create a DataFrame for preprocessing (important for ColumnTransformer)
            input_df = pd.DataFrame([input_data])

            # Apply the preprocessor
            processed_input = hypertension_preprocessor.transform(input_df)

            # Make prediction
            prediction_proba = hypertension_model.predict(processed_input)[0][0]
            prediction_class = (prediction_proba > 0.5).astype(int)

            result = "Hypertension" if prediction_class == 1 else "No Hypertension"
            confidence = f"{prediction_proba * 100:.2f}%"

            return jsonify({'prediction': result, 'confidence': confidence})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return render_template('hypertension.html')

@app.route('/predict_stroke', methods=['GET', 'POST'])
def predict_stroke():
    if request.method == 'POST':
        if not stroke_model or not stroke_preprocessor:
            return jsonify({'error': 'Stroke model or preprocessor not loaded properly.'}), 500

        try:
            data = request.form.to_dict()
            # Convert to appropriate types
            input_data = {
                'sex': float(data['sex']), # Assuming 0 or 1
                'age': float(data['age']),
                'hypertension': float(data['hypertension']), # Assuming 0 or 1
                'heart_disease': float(data['heart_disease']), # Assuming 0 or 1
                'ever_married': float(data['ever_married']), # Assuming 0 or 1
                'work_type': float(data['work_type']),
                'Residence_type': float(data['Residence_type']), # Assuming 0 or 1
                'avg_glucose_level': float(data['avg_glucose_level']),
                'bmi': float(data['bmi']),
                'smoking_status': float(data['smoking_status'])
            }
            
            # Create a DataFrame for preprocessing (important for ColumnTransformer)
            input_df = pd.DataFrame([input_data])

            # Apply the preprocessor
            processed_input = stroke_preprocessor.transform(input_df)

            # Make prediction
            prediction_proba = stroke_model.predict(processed_input)[0][0]
            prediction_class = (prediction_proba > 0.5).astype(int)

            result = "Stroke Risk" if prediction_class == 1 else "Low Stroke Risk"
            confidence = f"{prediction_proba * 100:.2f}%"

            return jsonify({'prediction': result, 'confidence': confidence})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return render_template('stroke.html')

if __name__ == '__main__':
    app.run(debug=True) # Set debug=False for production