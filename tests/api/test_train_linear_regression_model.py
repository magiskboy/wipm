"""
@Author: NguyenKhacThanh
"""

import pytest
from voluptuous import All, Required, Schema, Range
from tests.api import APITestCase


@pytest.mark.usefixtures("inject_data", "inject_push_data", "inject_func_call_create_model")
class TrainLinearRegressionTestCase(APITestCase):
    def method(self):
        return "PUT"

    def url(self):
        return "/regression/linear_regression"

    def test_success(self):
        id_model = self.create_model("linear_regression")
        payload = {
            "id_model": id_model,
            "id_dataset": self.id_dataset
        }
        code, body = self.call_api(
            content=payload
        )

        assert 200 == code, body.get("message", "")

        schema = Schema({
            Required("mean_squared_error"): All(float, Range(min=0)),
            Required("mean_absolute_error"): All(float, Range(min=0))
        })
        schema(body)

    def test_not_found_model(self):
        payload = {
            "id_model": "123456781234567812345678",
            "id_dataset": self.id_dataset
        }
        code, body = self.call_api(
            content=payload
        )

        assert 400 == code, body.get("message", "")

        schema = Schema({
            Required("message"): str,
        })
        schema(body)

    def test_not_found_dataset(self):
        id_model = self.create_model("linear_regression")
        payload = {
            "id_model": id_model,
            "id_dataset": "123456789123456712345678"
        }
        code, body = self.call_api(
            content=payload
        )

        assert 400 == code, body.get("message", "")

        schema = Schema({
            Required("message"): str,
        })
        schema(body)
