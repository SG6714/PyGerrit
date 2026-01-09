# PyGerritAPI Application

This project is a Flask-based web application that interfaces with the native Gerrit REST API. It provides endpoints to fetch information about users, projects, and changes from the Gerrit server and presents them through a simple retro-themed web interface.

## Features

- List all active Gerrit users and compare them to a CSV list of AD employees.
- Retrieve and display Gerrit projects.
- Fetch and display open changes in Gerrit.
- Retro-themed web interface for a nostalgic user experience.

## Getting Started

### Prerequisites

**For Docker (Recommended):**
- Docker
- Docker Compose

**For Local Development:**
- Python 3.x
- pip (Python package installer)

### Installation

#### Docker Installation (Recommended)

1. **Clone the Repository**
```
git clone https://github.com/SG6714/pygerrit.git
cd pygerrit
```

2. **Configure Environment Variables**
```bash
cp .env.example .env
# Edit .env file with your Gerrit credentials
```

#### Local Installation

1. **Clone the Repository**
```
git clone https://github.com/SG6714/pygerrit.git
cd pygerrit
```


2. **Create a Virtual Environment**
It’s a good practice to use a virtual environment for Python projects.
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```


3. **Install Dependencies**
Install the required Python packages using pip.
```
pip install -r requirements.txt
```


4. **Set Environment Variables**
Create a .env file or set these variables in your environment:
```
SECRET_KEY=your_secret_key
GERRIT_URL=your_gerrit_url:port
GERRIT_USERNAME=your_gerrit_username
GERRIT_PASSWORD=your_gerrit_password
FLASK_ENV=development  # Set to 'production' for production environment
```


## Running the Application

### Option 1: Using Docker Compose (Recommended)

1. **Copy the example environment file**
   ```bash
   cp .env.example .env
   ```

2. **Edit the .env file**
   Update the `.env` file with your Gerrit credentials:
   ```
   GERRIT_URL=https://your-gerrit-server.com:8080
   GERRIT_USERNAME=your_username
   GERRIT_PASSWORD=your_gerrit_api_token
   ```

3. **Start the application**
   ```bash
   docker compose up
   ```
   
   To run in detached mode:
   ```bash
   docker compose up -d
   ```

4. **Stop the application**
   ```bash
   docker compose down
   ```

> The app will be available at http://localhost:5000.

### Option 2: Running Locally

#### Start the Flask App
Run the following command to start the Flask development server:
```
python app.py
```
> By default, the app will be available at http://localhost:5000.


### Access the Application

Open your web browser and go to http://localhost:5000 to access the retro-themed dashboard.


## Usage
* **Login Page**: Enter your Gerrit username and API token to authenticate.
* **Dashboard**: Use the buttons to fetch and display data from the Gerrit server.
    * **Users**: Displays a list of active users.
    * **Projects**: Lists all projects.
    * **Changes**: Shows open changes.



## Project Structure
* /api: Contains the modules for interacting with the Gerrit API.
    * users.py: Manages user-related API calls.
    * projects.py: Manages project-related API calls.
    * changes.py: Manages change-related API calls.
* /templates: Contains HTML templates for the web interface.
    * index.html: Main dashboard interface.
    * login.html: Login form interface.
* app.py: Main application file.
* config.py: Configuration settings for different environments.
* requirements.txt: Python dependencies.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
If you’d like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## Troubleshooting

* Authentication Errors: Ensure your Gerrit URL and credentials are correct.
* Dependency Issues: Ensure all required Python packages are installed using the provided requirements.txt.

> For further help, please open an issue on GitHub.

### Key Points

- **Environment Variables**: The guide suggests setting them either through a `.env` file or directly in the environment, which is a common practice for managing secrets and configurations.
- **Virtual Environment**: Encourages using a virtual environment to avoid dependency conflicts.
- **Running Instructions**: Clear steps to start the Flask server and access the application.
- **Project Structure**: Provides an overview of the directory layout and purpose of each component.
- **Troubleshooting**: Basic guidance for common issues users might face.
