from fastapi import FastAPI
import mlflow.pyfunc
from mlflow.tracking import MlflowClient
import json
import numpy as np

app = FastAPI()

server_uri = "http://antoniomlflowaci.westeurope.azurecontainer.io:5000"
mlflow.set_tracking_uri(server_uri)
client = MlflowClient()

model_name = "tree_model"
last_version = client.get_registered_model(model_name).latest_versions[0].version
model = mlflow.sklearn.load_model(f"models:/{model_name}/{last_version}")


@app.get('/')
def get_root():
    return {'message': 'Iris flower detection API'}


@app.get('/predict_iris/')
async def predict_iris(flower_data: str):
    data = json.loads(flower_data)
    data = np.array(list(data.values())).reshape(1, -1)
    prediction = model.predict(data)
    return {"prediction": str(prediction[0])}
