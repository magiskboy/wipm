import pytest


@pytest.fixture
def client_class(request, client):
    if request.cls is not None:
        request.cls.client = client
