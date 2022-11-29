from app import app

# Upload file
@app.route("/file", methods=["POST"])
def uploadFile():
    return "file uploader"