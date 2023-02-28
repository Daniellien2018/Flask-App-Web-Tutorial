from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

#note model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # date = db.Column(db.DateTime(timezone=True), default=func.now) #get current time
    #association, one user to many notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

#user model
class User(db.Model, UserMixin): #define schema of users
    #column = db.Column(type)
    #db.Column(db.String(max length))
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #user has many notes 
    notes = db.relationship('Note')
    