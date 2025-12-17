# Load Model
import joblib
from schema.pydantic import IrisFeatures
model = joblib.load("model/iris_model.pkl")


model_version='1.0.0'


def predict(features):
    prediction = model.predict([features])
    return prediction
