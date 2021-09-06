import requests
from mlflow.tracking import MlflowClient
import mlflow


MODEL_URI = "http://antonioirismodelaci.westeurope.azurecontainer.io:8000/predict_iris"
MLFLOW_URI = "http://antoniomlflowaci.westeurope.azurecontainer.io:5000"
MLFLOW_EXP_NAME = "tree_model_iris"
MLFLOW_MODEL_NAME = "tree_model"
MODEL_ACC_KPI = 0.9

mlflow.set_tracking_uri(MLFLOW_URI)
client = MlflowClient()


def test_valid_request(valid_request_data):
    """
    Tests a valid request is processed successfully.
    """
    prediction = requests.get(MODEL_URI, {"flower_data": valid_request_data})
    assert prediction.status_code == 200


def test_request_wrong_datatype_fails(request_data_wrong_type):
    """
    Tests a request with the wrong data types is not processed successfully.
    """
    prediction = requests.get(MODEL_URI, {"flower_data": request_data_wrong_type})
    assert prediction.status_code != 200


def test_request_wrong_schema_fails(request_data_bad_schema):
    """
    Tests a request with the wrong schema is not processed successfully.
    """
    prediction = requests.get(MODEL_URI, {"flower_data": request_data_bad_schema})
    assert prediction.status_code != 200
