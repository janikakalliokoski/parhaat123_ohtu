from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///seppaemi"
=======
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///jbkallio"
>>>>>>> c081ab72885d2259724c48e49763f358bd73434b
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
