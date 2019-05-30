"""Test delete dataset
@Author: NguyenKhacThanh
"""

import pytest
from tests.api import APITestCase


@pytest.mark.usefixtures("inject_data")
class DeleteDatasetTestCase(APITestCase):
    def url(self):
        return "/dataset/"

    def method(self):
        return "DELETE"

    def test_success(self):
        # push data
        self.call_api(
            url=f"/dataset/{self.id_dataset}",
            method="PUT",
            content=self.payload
        )

        # delete dataset
        code, body = self.call_api(
            url=f"/dataset/{self.id_dataset}"
        )
        assert 200 == code, body["message"]

    def test_id_dataset_not_found(self):
        code, body = self.call_api(
            url="/dataset/123456781234567812345678",
            content=self.payload
        )
        assert 400 == code, body["message"]

    def test_id_dataset_invalid(self):
        code, body = self.call_api(
            url=f"/dataset/id_dataset_invalid"
        )
        assert code == 400, body["message"]
