from flask import Flask
from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)

# Select the configuration based on environment
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)
