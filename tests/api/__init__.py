import unittest
import pytest


@pytest.mark.usefixtures("client")
@pytest.mark.usefixtures("client_class")
class APITestCase(unittest.TestCase):
    def call_api(self, url=None, method=None, content=None):
        """Send request to server
        :param: url, str
        :param: method, str
        :content: dict
        :return: only return (status_code, json_data)
        """
        url = "/api/v1" + (url or self.url())
        method = method or self.method()
        sender = getattr(self.client, method.lower())
        response = None
        if content:
            response = sender(url, json=content)
        else:
            response = sender(url)
        return response.status_code, response.get_json()

    def url(self):
        """Setup api url
        """
        raise NotImplementedError("Url must provide")

    def method(self):
        """Setup api method
        """
        raise NotImplementedError("Method must provide")
