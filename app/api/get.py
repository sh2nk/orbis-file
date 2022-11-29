from app import app

# Get all files list
@app.route("/files")
def getFiles():
    return "files list"

# Get file data
@app.route("/file/<file_id>")
def getFile(file_id=''):
    return "file id %s data get" % file_id