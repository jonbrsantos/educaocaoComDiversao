import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "senha_admin")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///local.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
