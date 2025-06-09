document.addEventListener('DOMContentLoaded', () => {
    // Function to handle form submission for all prediction pages
    const handlePredictionForm = (formId, resultId, endpoint) => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', async (event) => {
                event.preventDefault(); // Prevent default form submission

                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries());

                const resultDiv = document.getElementById(resultId);
                resultDiv.innerHTML = 'Predicting...';
                resultDiv.style.backgroundColor = '#FFFBE6'; // Light yellow for loading
                resultDiv.style.color = '#B58800'; // Darker yellow for loading

                try {
                    const response = await fetch(endpoint, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded', // Or 'application/json' if sending JSON
                        },
                        body: new URLSearchParams(data).toString(), // For x-www-form-urlencoded
                        // If sending JSON: body: JSON.stringify(data),
                    });

                    const result = await response.json();

                    if (response.ok) {
                        resultDiv.innerHTML = `Prediction: <strong>${result.prediction}</strong><br>Confidence: ${result.confidence}`;
                        resultDiv.style.backgroundColor = '#E6FFE6'; // Light green for success
                        resultDiv.style.color = '#388E3C'; // Darker green for success
                    } else {
                        resultDiv.innerHTML = `Error: ${result.error || 'Something went wrong.'}`;
                        resultDiv.style.backgroundColor = '#FFCCCC'; // Light red for error
                        resultDiv.style.color = '#D32F2F'; // Darker red for error
                    }
                } catch (error) {
                    console.error('Fetch error:', error);
                    resultDiv.innerHTML = `Network Error: Could not connect to the server.`;
                    resultDiv.style.backgroundColor = '#FFCCCC';
                    resultDiv.style.color = '#D32F2F';
                }
            });
        }
    };

    // Apply to each prediction form
    handlePredictionForm('diabetes-form', 'diabetes-prediction-result', '/predict_diabetes');
    handlePredictionForm('hypertension-form', 'hypertension-prediction-result', '/predict_hypertension');
    handlePredictionForm('stroke-form', 'stroke-prediction-result', '/predict_stroke');
});