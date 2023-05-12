from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

model = joblib.load("model.joblib")


def make_prediction(inputs):
    """
    Make a prediction using the trained model
    """
    predictions = model.predict([inputs])
    return predictions

@app.route("/", methods=["GET"])
def index():
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to my Flask API: Text Classification Model</h1>"
        "</body>"
        "</html>"
    )
    return body

@app.route('/predict', methods=['POST'])
def predict():
    data_json = request.get_json()
    text = data_json['text']  # Assuming the JSON input has a 'text' field

    prediction = make_prediction(text)

    if prediction == 0:
        prediction = 'Not COVID-19 related'
    elif prediction == 1:
        prediction = 'COVID-19 related'

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run()
