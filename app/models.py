from datetime import datetime, timezone
from app import db

class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    extension = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Integer(), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    comment = db.Column(db.String())

    def __init__(self, name, extension, size, path, comment):
        self.name = name
        self.extension = extension
        self.size = size
        self.path = path
        self.comment = comment

    def __repr__(self):
        return f"<File {self.name}>"