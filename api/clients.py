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

    def get(self, endpoint, params=None, **kwargs):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            params=params,
            timeout=self.timeout,
            **kwargs
        )

    def post(self, endpoint, payload=None, **kwargs):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout,
            **kwargs
        )

    def put(self, endpoint, payload=None, **kwargs):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout,
            **kwargs
        )

    def patch(self, endpoint, payload=None, **kwargs):
        return self.session.patch(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )
