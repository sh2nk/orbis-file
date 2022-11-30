from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
import os

app = Flask(__name__)
app.config.from_object(os.environ.get("FLASK_ENV") or "config.DevConfig")

db = SQLAlchemy(app)
migrate = Migrate(app,  db)

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

from . import dbsync
from . import api
from . import models