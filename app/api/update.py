from app import app, db
from app.models import File
from flask import request, jsonify
from pathlib import Path
import os, shutil

@app.route("/file/<file_id>", methods=["PUT"])
def update_file(file_id=''):
    if not request.is_json:
        return jsonify({"error": "Request doesn't contain any valid JSON"}), 400
    
    data = request.get_json()
    file = File.query.get_or_404(file_id)

    if "name" in data.keys():
        file.name = data["name"]
    if "comment" in data.keys():
        file.comment = data["comment"]
    if "path" in data.keys(): # very evil stuff, unsafe as f.
        p = Path(data["path"])
        if not p.exists():
            os.mkdir(data["path"])
        shutil.move(os.path.join(file.path, file.id+file.extension), \
                    os.path.join(data["path"], file.id+file.extension))
        file.path = data["path"]

    db.session.add(file)
    db.session.commit()

    return {"message": "file id %s updated succsessfully" % file.id}