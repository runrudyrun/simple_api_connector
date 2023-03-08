import requests

class APIConnector:
    def __init__(self, api_url, api_key=None):
        self.api_url = api_url
        self.api_key = api_key

    def get_data(self):
        headers = {}
        if self.api_key:
            headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.get(self.api_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get data. Status code: {response.status_code}")
            