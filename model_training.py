import mlflow
from mlflow.tracking import MlflowClient
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

server_uri = "http://antoniomlflowaci.westeurope.azurecontainer.io:5000"
exp_name = "tree_model_iris"
model_name = "tree_model"
artifact_path = "mlflow-artifact-root"
params = {"max_depth": 10, "max_features": 4, "min_samples_split": 5, "random_state": 1}

mlflow.set_tracking_uri(server_uri)
client = MlflowClient()
exp_names = [exp.name for exp in client.list_experiments()]
if exp_name not in exp_names:
    client.create_experiment(exp_name)
exp = client.get_experiment_by_name(exp_name)

iris = datasets.load_iris()
x, y = iris.data, iris.target
labels = iris.target_names
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=1)

with mlflow.start_run(experiment_id=exp.experiment_id) as run:
    tree = DecisionTreeClassifier(**params)
    tree.fit(x_train, y_train)
    y_pred = tree.predict(x_test)

    mlflow.log_params(tree.get_params())
    mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
    mlflow.sklearn.log_model(tree, "mlflow-artifact-root")
    model_uri = f"runs:/{run.info.run_id}/{artifact_path}"
    mv = mlflow.register_model(model_uri, "tree_model")
