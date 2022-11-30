from app import app, db
from app.models import File
from flask import request, jsonify

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
    if "path" in data.keys():
        file.path = data["path"]

    db.session.add(file)
    db.session.commit()

    return {"message": "file id %d updated succsessfully" % file.id}