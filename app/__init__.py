from flask import Flask
from .config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
from flask_wtf.csrf import CSRFProtect
app.config.from_object(Config)

from app import views