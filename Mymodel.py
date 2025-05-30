from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
import pickle

# Initialize Flask app
app = Flask(_name_)

# Load your pre-trained model from the pickle (.pkl) file
MODEL_PATH = "path_to_your_model/model.pkl"  # Adjust this path to your model
with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

# Define the folder to save the uploaded images (optional)
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Define the route to handle the prediction
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        # Load and preprocess the image
        image = cv2.imread(filepath)
        image = cv2.resize(
            image, (224, 224)
        )  # Resize image to the input size expected by your model (adjust as needed)

        # Normalize the image if necessary (example: divide by 255 for pixel scaling)
        image = image.astype("float32") / 255.0

        # Reshape the image to match model input shape (batch size, height, width, channels)
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Predict using the loaded model
        prediction = model.predict(image)

        # Process the prediction (assuming the model returns a class index or name)
        disease_name = prediction[
            0
        ]  # Assuming the model returns a list or array, take the first result

        # Return the result as a JSON response
        return jsonify({"prediction": disease_name})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the app
if _name_ == "_main_":
    app.run(debug=True)
