"""Test delete model
@Author: NguyenKhacThanh
"""

import pytest
from voluptuous import Schema, All, Required
from tests.api import APITestCase

@pytest.mark.usefixtures("inject_client", "inject_params_model_regression")
class DeleteModelTestCase(APITestCase):
    def url(self):
        return "/regression"

    def method(self):
        return "DELETE"

    def test_success(self):
        # push data
        res = self.client.post(
            "/api/v1/regression/huber",
            json=self.params["huber"]
        )
        code, body = self.call_api(
            url=f"/regression/{res.get_json()['id']}",
        )
        schema = Schema({
            Required("message"): str
        })

        schema(body)
        assert 200 == code, body["message"]

    def test_id_model_not_found(self):
        code, body = self.call_api(
            url="/regression/123456781234567812345678",
        )
        schema = Schema({
            Required("message"): str
        })
        schema(body)
        assert 400 == code, body["message"]
