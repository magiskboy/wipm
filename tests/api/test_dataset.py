import numpy as np
from voluptuous import Schema, All, Required, Length
from tests.api import APITestCase


class CreateDatasetTestCase(APITestCase):
    def url(self):
        return "/dataset/"

    def method(self):
        return "POST"

    def test_success(self):
        payload = {
            "number_of_input": 3
        }
        code, body = self.call_api(content=payload)
        assert 200 == code, body["message"]
        schema = Schema({
            Required("id"): All(str, Length(24)),
            Required("message"): str
        })
        schema(body)

    def test_none_payload(self):
        payload = {}
        code, body = self.call_api(content=payload)
        assert 400 == code, body["message"]

    def test_no_input_less_than_one(self):
        payload = {
            "number_of_input": 0
        }
        code, body = self.call_api(content=payload)
        assert 400 == code, body["message"]


class PushDatasetTestCase(APITestCase):
    def url(self):
        return "/dataset/"

    def method(self):
        return "PUT"

    def test_success(self):
        payload = {
            "inputs": np.random.rand(10, 3).tolist(),
            "target": np.random.rand(10,).tolist()
        }
        id_dataset = self._create_dataset(3)
        code, body = self.call_api(
            url=f"/dataset/{id_dataset}",
            content=payload
        )
        assert 200 == code, body["message"]
        schema = Schema({
            Required("message"): str
        })
        schema(body)

    def _create_dataset(self, n=3):
        """Create dataset before
        :return: id_dataset, str
        """
        code, body = self.call_api(
            url="/dataset/",
            method="POST",
            content={"number_of_input": n}
        )
        return body["id"]


class DeleteDatasetTestCase(APITestCase):
    def url(self):
        return "/dataset/"

    def method(self):
        return "DELETE"

    def test_success(self):
        id_dataset = self._create_dataset(3)
        code, body = self.call_api(url=f"/dataset/{id_dataset}")
        assert 200 == code, body["message"]
        schema = Schema({
            Required("message"): str
        })
        schema(body)

    def _create_dataset(self, n=3):
        """Create dataset before
        :return: id_dataset, str
        """
        code, body = self.call_api(
            url="/dataset/",
            method="POST",
            content={"number_of_input": n}
        )
        print(body)
        return body["id"]
