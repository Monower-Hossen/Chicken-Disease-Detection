import os
from flask import Flask, request, render_template, jsonify
from chicken_classifier.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# Define a temporary upload folder relative to the project root
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=['GET'])
def home():
    """
    Renders the home page of the web application.
    """
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict_route():
    """
    Handles image upload and returns the prediction from the model.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        try:
            obj = PredictionPipeline(filepath)
            prediction_result = obj.predict()
            return jsonify(prediction_result[0]) # PredictionPipeline returns [{"image": "Prediction_Label"}]
        except Exception as e:
            return jsonify({"error": f"Prediction failed: {str(e)}"}), 500
        finally:
            os.remove(filepath) # Clean up the temporary file

if __name__ == "__main__":
    # Run the Flask app
    # For local development, you can use debug=True for automatic reloading
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(host='0.0.0.0', port=8080)