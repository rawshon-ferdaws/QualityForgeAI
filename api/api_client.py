import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint, headers=None, params=None):
        return requests.get(
            self.base_url + endpoint,
            headers=headers,
            params=params
        )

    def post(self, endpoint, payload=None, headers=None):
        return requests.post(
            self.base_url + endpoint,
            json=payload,
            headers=headers
        )

    def put(self, endpoint, payload=None, headers=None):
        return requests.put(
            self.base_url + endpoint,
            json=payload,
            headers=headers
        )

    def delete(self, endpoint, headers=None):
        return requests.delete(
            self.base_url + endpoint,
            headers=headers
        )
