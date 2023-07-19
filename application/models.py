from datetime import datetime
from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_role = db.Column(db.String(20), default='user')
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}', user_role='{self.user_role}', join_date='{self.join_date}')"
