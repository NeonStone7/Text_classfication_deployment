import joblib

model = joblib.load("model_text_class.joblib")

def make_prediction(inputs):
    """
    Make a prediction using the trained model
    """
    predictions = model.predict([inputs])
    return predictions[0]
