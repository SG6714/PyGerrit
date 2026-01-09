import os
from flask import Flask, jsonify, request
from api.users import GerritUserManager
from api.projects import GerritProjectManager
from api.changes import GerritChangeManager

app = Flask(__name__)

# Get configuration from environment variables
GERRIT_URL = os.environ.get('GERRIT_URL', '')
USERNAME = os.environ.get('GERRIT_USERNAME', '')
PASSWORD = os.environ.get('GERRIT_PASSWORD', '')


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

@app.route('/api/project_changes', methods=['GET'])
def get_project_changes():
    try:
        projects = project_manager.get_projects()
        for project in projects:
            project = change_manager.get_project_changes(project[0])
        return jsonify(projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/changes', methods=['GET'])
def get_changes():
    try:
        changes = change_manager.get_changes(10)
        return jsonify(changes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/fte_users', methods=['GET'])
def get_users():
    try:
        gerrit_users = get_users()
        csv_users = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                csv_users.append(row)
        results = user_manager.compare_users(gerrit_users, csv_users)
        
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

