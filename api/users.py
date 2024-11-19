import requests
from requests.auth import HTTPBasicAuth
import json

class GerritUserManager:
    def __init__(self, gerrit_url, username, password):
        self.gerrit_url = gerrit_url
        self.auth = HTTPBasicAuth(username, password)

    def list_all_active_users(self):
        count = 0
        user_list = []
        while True:
            api_endpoint = f'{self.gerrit_url}/a/accounts/?q=is:active&start={count}&limit=500&o=DETAILS'
            response = requests.get(api_endpoint, auth=self.auth)
            if response.status_code == 200:
                content = json.loads(response.text.split(")]}'\n")[1])
                user_list.extend(content)
                if "_more_accounts" not in content[-1]:
                    break
                count += len(content)
            else:
                raise Exception(f'Failed to retrieve users: {response.status_code} {response.reason}')
        return user_list

    def compare_users(self, json_users, csv_users):
        results = []
        csv_user_set = {user['User Account']: user for user in csv_users}
        for json_user in json_users:
            try:
                username = json_user['username'].upper()
                if username in csv_user_set:
                    json_user['status'] = "exists in both JSON and CSV."
                else:
                    json_user['status'] = "does NOT exist in CSV."
            except Exception as e:
                json_user['status'] = f"Unknown {e}"
            results.append(json_user)
        return results
