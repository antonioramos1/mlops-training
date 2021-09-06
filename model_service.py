from fastapi import FastAPI
import mlflow.pyfunc
import json
import numpy as np

app = FastAPI()

model_name = "tree_model"
version = '1'
server_uri = "http://antoniomlflowaci.westeurope.azurecontainer.io:5000"
mlflow.set_tracking_uri(server_uri)
model = mlflow.sklearn.load_model(f"models:/{model_name}/{version}")


@app.get('/')
def get_root():
    return {'message': 'Iris flower detection API'}


@app.get('/predict_iris/')
async def predict_iris(flower_data: str):
    data = json.loads(flower_data)
    data = np.array(list(data.values())).reshape(1, -1)
    prediction = model.predict(data)
    return {"prediction": str(prediction[0])}
