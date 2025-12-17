from fastapi import FastAPI
from model.predict import predict,model_version
from schema.pydantic import IrisFeatures
#model
from model.predict import model
import numpy as np

app = FastAPI()





@app.get("/")
def home():
    return {"message": "Iris Prediction API is running"}


@app.get("/health")
def health_check():
    return {
        "status":"OK",
        "model_version":model_version

    }

@app.post("/predict")
def predict(data: IrisFeatures):
    features = np.array([[data.sepal_length, data.sepal_width,
                          data.petal_length, data.petal_width]])
    try:
        prediction = model.predict(features)[0]

        return {"prediction": str(prediction)}
    except Exception as e:
        return {"error": str(e)}
