from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

from features.url_features import extract_url_features

app = Flask(__name__)
CORS(app)

# ===============================
# Load trained ML model
# ===============================
with open("model/phishing_model.pkl", "rb") as f:
    model = joblib.load("model/phishing_model.pkl")
print("✅ Phishing model loaded successfully")
# ===============================
# Prediction API
# ===============================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    url = data["url"]

    # Extract features
    features = extract_url_features(url)
    features_np = np.array(features).reshape(1, -1)

    # Prediction
    prediction = model.predict(features_np)[0]
    probability = model.predict_proba(features_np)[0]

    phishing_prob = round(float(probability[1]) * 100, 2)
    legit_prob = round(float(probability[0]) * 100, 2)

    if prediction == 1:
        result = "phishing"
        confidence = phishing_prob
        explanation = "The URL exhibits suspicious structural patterns commonly associated with phishing attacks."
    else:
        result = "legitimate"
        confidence = legit_prob
        explanation = "The URL does not show significant phishing-related characteristics."

    return jsonify({
        "url": url,
        "prediction": result,
        "confidence": confidence,
        "explanation": explanation
    })


if __name__ == "__main__":
    app.run(debug=True)
