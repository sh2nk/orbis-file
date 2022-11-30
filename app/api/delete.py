from app import app, db
from app.models import File
import os

@app.route("/file/<file_id>", methods=["DELETE"])
def delete_file(file_id=''):
    file = File.query.get_or_404(file_id)
    os.remove(os.path.join(file.path, file.id+file.extension))
    db.session.delete(file)
    db.session.commit()
    
    return {"message": "file id %s deleted succsessfully" % file.id}