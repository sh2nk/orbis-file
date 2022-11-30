from app import app, db
from app.models import File
from flask import request, abort, jsonify
from werkzeug.utils import secure_filename
import os, uuid, pathlib

class Filename:
    def __init__(self, name='', uuid=None) -> None:
        if type(name) == str:
            path = pathlib.Path(name)
            exts = path.suffixes
            
            for e in exts:
                path = path.stem
                path = pathlib.Path(path)

            self.__name = str(path)
            self.__ext = "".join(exts)
            self.__uuid = uuid
        else:
            raise ValueError("Filename should be string!")

    def __call__(self, *args, **kwds) -> str:
        return self.__name

    def get_name(self):
        return self.__name

    def get_ext(self):
        return self.__ext

    def make_id(self):
        if not self.__uuid:
            self.__uuid = str(uuid.uuid4()) + self.__ext
        return self.__uuid

    def is_disabled(self):
        return self.__ext in app.config["DISABLED_EXTENSIONS"]


# Upload file
@app.route("/file/<comment>", methods=["POST"])
def uploadFile(comment=""):
    if "file" not in request.files:
        abort(400, description="Missing file part")
        
    raw = request.files["file"]
    filename = Filename(secure_filename(raw.filename))

    if filename() == '':
        return jsonify({"error": "Empty filename"}), 400

    if not raw:
        return jsonify({"error": "Empty file part"}), 400

    if not filename.is_disabled():
        fileid = filename.make_id()
        path = os.path.join(app.config['UPLOAD_FOLDER'], fileid)
        
        raw.save(path)
        size = os.stat(path).st_size

        file = File(name=filename.get_name(), \
                    extension=filename.get_ext(), \
                    size=size, \
                    path=app.config['UPLOAD_FOLDER'], \
                    comment=comment)

        db.session.add(file)
        db.session.commit()
    else:
        return jsonify({"error": "This file extension is disabled"}), 400
    
    return {"message": "Added %s succsesfully" % (file.name + file.extension)}
