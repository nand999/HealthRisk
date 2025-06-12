document.addEventListener('DOMContentLoaded', () => {
    const handlePredictionForm = (formId, resultId, endpoint, loadingSpinnerId, clearButtonId) => {
        const form = document.getElementById(formId);
        const loadingSpinner = document.getElementById(loadingSpinnerId);
        const clearButton = document.getElementById(clearButtonId);

        if (form) {
            form.addEventListener('submit', async (event) => {
                event.preventDefault(); 

                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries());

                const resultDiv = document.getElementById(resultId);
                if (loadingSpinner) loadingSpinner.style.display = 'block'; 
                resultDiv.innerHTML = ''; 


                try {
                    const response = await fetch(endpoint, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded', 
                        },
                        body: new URLSearchParams(data).toString(), 
                    });

                    const result = await response.json();

                    if (response.ok) {
                        resultDiv.innerHTML = `Prediction: <strong>${result.prediction}</strong><br>Confidence: ${result.confidence}`;
                        resultDiv.style.backgroundColor = '#E6FFE6'; 
                        resultDiv.style.color = '#388E3C'; 
                    } else {
                        resultDiv.innerHTML = `Error: ${result.error || 'Something went wrong.'}`;
                        resultDiv.style.backgroundColor = '#FFCCCC'; 
                        resultDiv.style.color = '#D32F2F'; 
                    }
                } catch (error) {
                    console.error('Fetch error:', error);
                    resultDiv.innerHTML = `Network Error: Could not connect to the server.`;
                    resultDiv.style.backgroundColor = '#FFCCCC';
                    resultDiv.style.color = '#D32F2F';
                } finally {
                    if (loadingSpinner) loadingSpinner.style.display = 'none'; 
                }
            });

            if (clearButton) {
                clearButton.addEventListener('click', () => {
                    form.reset();
                    const resultDiv = document.getElementById(resultId);
                    if (resultDiv) {
                        resultDiv.innerHTML = '';
                        resultDiv.style.backgroundColor = 'transparent'; 
                    }
                });
            }
        }
    };

    handlePredictionForm('diabetes-form', 'diabetes-prediction-result', '/predict_diabetes', 'loading-spinner', 'clear-diabetes-form');
    handlePredictionForm('hypertension-form', 'hypertension-prediction-result', '/predict_hypertension', 'loading-spinner', 'clear-hypertension-form');
    handlePredictionForm('stroke-form', 'stroke-prediction-result', '/predict_stroke', 'loading-spinner', 'clear-stroke-form');
});