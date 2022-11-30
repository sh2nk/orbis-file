import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BasicConfig:
    DEBUG = False

class DevConfig(BasicConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI") or "postgres://user:password@localhost:5432/orbis-file"