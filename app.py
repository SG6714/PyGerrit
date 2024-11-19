from flask import Flask, jsonify, request
from api.users import GerritUserManager
from api.projects import GerritProjectManager
from api.changes import GerritChangeManager

app = Flask(__name__)

# Replace with your actual Gerrit URL and credentials
GERRIT_URL = 'http://z61sp-gitapp01a.zebra.lan:8080'
USERNAME = 'your_username'
PASSWORD = 'your_password'

user_manager = GerritUserManager(GERRIT_URL, USERNAME, PASSWORD)
project_manager = GerritProjectManager(GERRIT_URL, USERNAME, PASSWORD)
change_manager = GerritChangeManager(GERRIT_URL, USERNAME, PASSWORD)

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        users = user_manager.list_all_active_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/projects', methods=['GET'])
def get_projects():
    try:
        projects = project_manager.get_projects()
        return jsonify(projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/changes', methods=['GET'])
def get_changes():
    try:
        changes = change_manager.get_changes()
        return jsonify(changes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

