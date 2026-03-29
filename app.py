from flask import Flask, request, jsonify
import gzip
import joblib

app = Flask(__name__)

# Load compressed model
with gzip.open("cybersecurity_model.pkl.gz", "rb") as f:
    model = joblib.load(f)

# Home route
@app.route('/')
def home():
    return "Cyber Threat Detection API is running!"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Get features
        features = data['features']

        # Fix shape issue
        if isinstance(features[0], list):
            prediction = model.predict(features)
        else:
            prediction = model.predict([features])

        return jsonify({
            "prediction": str(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)