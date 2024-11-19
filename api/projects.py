import requests
from requests.auth import HTTPBasicAuth
import json

class GerritProjectManager:
    def __init__(self, gerrit_url, username, password):
        self.gerrit_url = gerrit_url
        self.auth = HTTPBasicAuth(username, password)

    def get_projects(self):
        query = '/a/projects/?d'
        response = requests.get(self.gerrit_url + query, auth=self.auth)
        if response.status_code == 200:
            return self.clean_json(response.text)
        else:
            raise Exception(f"Failed to retrieve projects: {response.status_code}")

    @staticmethod
    def clean_json(content):
        data = content.replace(")]}'\n", "").replace('\n', '').replace("'", "").replace('\\"', '')
        return json.loads(data)
