import pytest
from wipm import create_app

__author__ = "NguyenKhacThanh"


@pytest.fixture(scope="class")
def client():
    app = create_app()
    return app.test_client()
