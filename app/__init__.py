from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object(os.environ.get("FLASK_ENV") or "config.DevConfig")

db = SQLAlchemy(app)
migrate = Migrate(app,  db)

from . import api
from . import models