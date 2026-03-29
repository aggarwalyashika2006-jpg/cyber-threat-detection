from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load trained model
model = joblib.load("cybersecurity_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Cybersecurity API is running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Validate input
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    if len(data) != 42:
        return jsonify({"error": f"Expected 42 features, got {len(data)}"}), 400

    try:
        # Convert to model input
        features = np.array([[data[str(i)] for i in range(42)]])

        # Prediction
        prediction = model.predict(features)

        return jsonify({"Threat_Detected": bool(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)