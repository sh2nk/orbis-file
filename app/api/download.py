from app import app, db
from app.models import File
from flask import send_file

# Download file
@app.route("/file/download/<int:file_id>")
def downloadFile(file_id=0):
    file = File.query.get_or_404(file_id)
    return send_file(path_or_file=file.path, \
                    as_attachment=True, \
                    download_name=file.name)