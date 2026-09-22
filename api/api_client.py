import requests

from utilities.config_reader import ConfigReader


class APIClient:

    def __init__(self):
        self.base_url = ConfigReader.get_api_base_url()
        self.timeout = ConfigReader.get_api_timeout()

        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint, params=None):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            params=params,
            timeout=self.timeout
        )

    def post(self, endpoint, payload=None):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout
        )

    def put(self, endpoint, payload=None):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout
        )

    def patch(self, endpoint, payload=None):
        return self.session.patch(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout
        )

    def delete(self, endpoint):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout
        )
