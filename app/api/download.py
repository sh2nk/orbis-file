from app import app

# Download file
@app.route("/file/download/<file_id>")
def downloadFile(file_id=''):
    return "downloader"