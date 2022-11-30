from app import app, db
from app.models import File
from flask import jsonify
from pathlib import Path

# Search file data
@app.route("/file/search/<path:query>")
def search_files(query=''):
    path = Path(query)
    print(path.stem)
    files = File.query.filter(File.name.like(f'%{path.stem}%') |\
                            File.extension.like(f'%{query}%') |\
                            File.path.match(query) |\
                            File.comment.like(f'%{path.stem}%')).all()
    return jsonify([f.to_dict() for f in files])