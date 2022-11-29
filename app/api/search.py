from app import app

# Search file data
@app.route("/file/search/<query>")
def searchFiles(query=''):
    return "searching for %s" % query