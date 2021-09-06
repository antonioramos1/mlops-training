import pytest
import json
from sklearn import datasets


iris = datasets.load_iris()
feat_names = iris.feature_names


@pytest.fixture
def valid_request_data():
    request_values = [5.8, 4., 1.2, 0.2]
    request_data = {feat_names[i]: request_values[i] for i in range(len(feat_names))}
    return json.dumps(request_data)


@pytest.fixture
def request_data_wrong_type():
    request_values = [5.8, 4., 1.2, "string"]
    request_data = {feat_names[i]: request_values[i] for i in range(len(feat_names))}
    return json.dumps(request_data)


@pytest.fixture
def request_data_bad_schema():
    request_values = [5.8, 4., 1.2, 0.2]
    clip_values = 2
    request_data = {feat_names[i]: request_values[i] for i in range(len(feat_names[:clip_values]))}
    return json.dumps(request_data)
