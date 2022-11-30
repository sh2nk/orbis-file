from app import app, db, utils
from app.models import File
from pathlib import Path
from sqlalchemy.dialects.postgresql import insert as pg_insert
import os, uuid

@app.cli.command("syncdb")
def db_sync():
    print(" * Starting db sync")
    paths = list()
    for path, subdirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        for name in files:
            paths.append(os.path.join(path, name))

    files_local = dict()
    files_remote = dict()
    for f in File.query.all():
        files_remote[f.id] = f

    for p in paths:
        path = Path(p)
        exts = "".join(path.suffixes)

        file = File(id=path.stem, \
            name=path.stem, \
            extension=exts, \
            size=os.stat(p).st_size, \
            path=str(path.parent), \
            comment="")

        if not utils.is_valid_uuid(path.stem):
            id = str(uuid.uuid4())
            file.id = id
            os.rename(path, os.path.join(str(path.parent), id+exts))

        files_local[path.stem] = file

    values = [files_local[f] for f in (files_local.keys() - files_remote.keys())]
    db.session.bulk_save_objects(values)
    db.session.commit()

    [db.session.delete(files_remote[f]) for f in (files_remote.keys() - files_local.keys())]
    db.session.commit()