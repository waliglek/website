from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    motdepasse=db.Column(db.String(150))
    nom=db.Column(db.String(150))