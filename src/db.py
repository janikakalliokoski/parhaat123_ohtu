from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///seppaemi"
=======
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///heinonos"
>>>>>>> b69491206a749821af70e43965936a19ec7ecd3d
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
