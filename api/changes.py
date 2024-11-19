import requests
from requests.auth import HTTPBasicAuth
import json

class GerritChangeManager:
    def __init__(self, gerrit_url, username, password):
        self.gerrit_url = gerrit_url
        self.auth = HTTPBasicAuth(username, password)

    def get_changes(self):
        count = 0
        change_list = []
        while True:
            query = f'/a/changes/?q=is:open&start={count}&limit=500&o=ALL_COMMITS'
            response = requests.get(self.gerrit_url + query, auth=self.auth)
            if response.status_code == 200:
                json_data = self.clean_json(response.text)
                change_list.extend(json_data)
                if not json_data or '_more_changes' not in json_data[-1]:
                    break
                count += len(json_data)
            else:
                raise Exception(f"Failed to retrieve changes: {response.status_code}")
        return change_list

    @staticmethod
    def clean_json(content):
        data = content.replace(")]}'\n", "").replace('\n', '').replace("'", "").replace('\\"', '')
        return json.loads(data)
