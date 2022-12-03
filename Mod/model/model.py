from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

db = SQLAlchemy()

class UserData(db.Model):
    __tablename__ = "userdata"
    __table_args__ = {'mysql_collate': 'utf8mb3_bin'}

    id = db.Column(db.String(13,"utf8mb3_bin"), primary_key=True, nullable=False)
    name = db.Column(db.String(5,"utf8mb3_bin"))
    pwhash = db.Column(db.String(64,"utf8mb3_bin"))
    grade = db.Column(db.Integer)
    ban = db.Column(db.Integer)
    email = db.Column(db.String(30,"utf8mb3_bin"), unique=True)
    def __init__(self, id, name, pwhash, grade, ban, email):
        self.id = id
        self.name = name
        self.pwhash = pwhash
        self.grade = grade
        self.ban = ban
        self.email = email
