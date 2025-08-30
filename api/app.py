from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from features.extract_features import extract_features

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend calls

# Load the model
model = joblib.load("models/url_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({"error": "Missing 'url' field"}), 400
    
    url = data['url']
    
    print(f"Analyzing URL: {url}")
    
    features = extract_features(url)
    features_df = [list(features.values())]
    prediction = model.predict(features_df)[0]
    result = "Unsafe" if prediction == 1 else "safe"

    return jsonify({"url": url, "result": result})

if __name__ == "__main__":
    app.run(debug=True)
