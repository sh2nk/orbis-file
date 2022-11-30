from app import app, db
from app.models import File
from flask import jsonify

# Get all files list
@app.route("/files")
def getFiles():
    files = File.query.all()
    return jsonify([f.to_dict() for f in files])

# Get file data
@app.route("/file/<file_id>")
def getFile(file_id=''):
    return "file id %s data get" % file_id