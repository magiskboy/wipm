"""
@Author: NguyenKhacThanh
"""

import pytest
from voluptuous import All, Required, Schema, Length
from tests.api import APITestCase


@pytest.mark.usefixtures("inject_params_model_regression")
class CreateLinearRegressionTestCase(APITestCase):
    def method(self):
        return "POST"

    def url(self):
        return "/regression/linear_regression"

    def test_success(self):
        payload = self.params["linear_regression"]
        code, body = self.call_api(
            content=payload
        )

        assert 200 == code, body.get("message", "")

        schema = Schema({
            Required("id"): All(str, Length(24)),
            "message": str
        })
        schema(body)
