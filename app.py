from flask import Flask, jsonify, request
from predict import make_prediction

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to my Flask API</h1>"
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
    else:
        prediction = 'COVID-19 related'

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run()