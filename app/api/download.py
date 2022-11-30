from app import app, db
from app.models import File
from flask import send_from_directory

# Download file
@app.route("/file/download/<file_id>")
def download_file(file_id=''):
    file = File.query.get_or_404(file_id)
    return send_from_directory(directory=file.path, \
                                path=file.id+file.extension, \
                                as_attachment=True, \
                                download_name=file.name+file.extension)