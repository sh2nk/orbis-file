from app import app, db
from app.models import File
from flask import request, abort, jsonify
from werkzeug.utils import secure_filename
import os, uuid

class Filename:
    def __init__(self, name='') -> None:
        if type(name) == str:
            self.__name = name
            self.__ext = name.rsplit('.', 1)[1].lower()
        else:
            raise ValueError("Filename should be string!")

    def __call__(self, *args, **kwds) -> str:
        return self.__name

    def getName(self):
        return self.__name

    def getExt(self):
        return ".%s" % self.__ext

    def getID(self):
        print(str(uuid.uuid4()))
        print(self.__name)
        print(self.__ext)
        return "%s.%s" % (str(uuid.uuid4()), self.__ext)

    def isDisabled(self):
        return '.' in self.__name and self.__ext in app.config["DISABLED_EXTENSIONS"]


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

    if not filename.isDisabled():
        fileid = filename.getID()
        path = os.path.join(app.config['UPLOAD_FOLDER'], fileid)
        
        raw.save(path)
        size = os.stat(path).st_size

        file = File(name=filename.getName(), \
                    extension=filename.getExt(), \
                    size=size, \
                    path=path, \
                    comment=comment)

        db.session.add(file)
        db.session.commit()
    else:
        return jsonify({"error": "This file extension is disabled"}), 400
    
    return {"message": "Added %s succsesfully" % file.name}
