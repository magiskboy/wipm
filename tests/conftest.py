"""Fixtures for test case
@Author: NguyenKhacThanh
"""

import os
import json
import pytest
from wipm import create_app


@pytest.fixture(scope="class")
def inject_client(request):
    """Inject flask client app into test case class
    """
    if not hasattr(request.cls, "client"):
        app = create_app()
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        setattr(request.cls, "client", app.test_client())
    yield


@pytest.fixture(scope="class")
def inject_data(request):
    client = request.cls.client
    with open(os.path.join("tests", "datafiles", "push_dataset.json"), "r") as f:
        payload = json.load(f)
    setattr(request.cls, "payload", payload)
    response = client.post(
        "/api/v1/dataset",
        json={"number_of_input": len(payload["inputs"][0])}
    )
    id_dataset = response.get_json().get("id")
    setattr(request.cls, "id_dataset", id_dataset)

    yield

    client.delete(f"/api/v1/dataset/{id_dataset}")


@pytest.fixture(scope="class")
def inject_params_model_regression(request):
    with open(os.path.join("tests", "datafiles", "params_regression_model.json"), "r") as f:
        params = json.load(f)
    setattr(request.cls, "params", params)

    yield


@pytest.fixture(scope="class")
def inject_push_data(request):
    client = request.cls.client
    res = client.put(
       f"/api/v1/dataset/{request.cls.id_dataset}",
       json=request.cls.payload
    )
    return


@pytest.fixture(scope="class")
def inject_func_call_create_model(request):
    client = request.cls.client
    with open(os.path.join("tests", "datafiles", "params_regression_model.json"), "r") as f:
        params = json.load(f)
    id_model = None
    def create_model(self, type_model):
        url = f"/api/v1/regression/{type_model}"
        response = client.post(url, json=params[type_model])
        id_model = response.get_json()["id"]
        return id_model
    setattr(request.cls, "create_model", create_model)

    yield

    client.delete(f"/api/v1/regressiopn/{id_model}")
