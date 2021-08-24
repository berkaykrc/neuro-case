from flask import Flask
import os
from neuro_case.views import main_page_bp

app = Flask(__name__)
environment_configuration = os.environ['CONFIGURATION_SETUP']
app.config.from_object(environment_configuration)

print(f"Environment: {app.config['ENV']}")
print(f"Debug: {app.config['DEBUG']}")
print(f"Secret key: {app.config['SECRET_KEY']}")

app.register_blueprint(main_page_bp)
