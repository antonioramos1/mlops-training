from mlflow.tracking import MlflowClient
import mlflow

MLFLOW_URI = "http://antoniomlflowaci.westeurope.azurecontainer.io:5000"
MLFLOW_EXP_NAME = "tree_model_iris"
MLFLOW_MODEL_NAME = "tree_model"
MODEL_ACC_KPI = 0.9

mlflow.set_tracking_uri(MLFLOW_URI)
client = MlflowClient()


def test_model_registered():
    """
    Tests the model is in the MLFlow registry.
    """
    assert client.get_registered_model(MLFLOW_MODEL_NAME)


def test_model_performance():
    """
    Tests whether the model reaches the performance KPI in the test dataset.
    """
    exp = client.get_experiment_by_name(MLFLOW_EXP_NAME)
    run_info = mlflow.list_run_infos(exp.experiment_id)[0]
    run = client.get_run(run_info.run_id)
    model_performance = run.data.metrics["accuracy"]
    assert model_performance >= MODEL_ACC_KPI
