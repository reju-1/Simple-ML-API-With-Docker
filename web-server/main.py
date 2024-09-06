from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

with open("svm_model_iris.pkl", "rb") as model_file:
    svm_model = pickle.load(model_file)

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

target_names = ['setosa', 'versicolor', 'virginica']

@app.post("/predict/")
def predict_iris(input_data: IrisInput):
    features = np.array([[input_data.sepal_length, input_data.sepal_width, 
                          input_data.petal_length, input_data.petal_width]])

    prediction = svm_model.predict(features)
    return {"prediction": target_names[int(prediction[0])]}

@app.get("/")
def read_root():
    return {"message": "Iris Prediction API is running"}
