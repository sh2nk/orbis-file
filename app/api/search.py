from app import app

# Search file data
@app.route("/file/search/<query>")
def search_files(query=''):
    return "searching for %s" % query