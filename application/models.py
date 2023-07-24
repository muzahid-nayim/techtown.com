from datetime import datetime
from application import db
from application import login_manager
from flask_login import UserMixin
from flask_wtf.file import FileField, FileAllowed

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# START USER MODAL 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_role = db.Column(db.String(20), default='user')
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}', user_role='{self.user_role}', join_date='{self.join_date}')"
# END USER MODAL 


# START BRAND MODAL 
class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    logo = db.Column(db.String(100), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Brand(id={self.id}, name='{self.name}', logo='{self.logo}')"
# END BRAND MODAL 