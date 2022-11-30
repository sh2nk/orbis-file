import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BasicConfig:
    DEBUG = False
    DISABLED_EXTENSIONS = {"html", "php"}

class DevConfig(BasicConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI") or "postgres://user:password@localhost:5432/orbis-file"
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER") or "./__storage__/"