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

# START PRODUCT MODEL 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_release = db.Column(db.String(100))
    colors = db.Column(db.String(100))
    price = db.Column(db.Integer)
    manufactured_by = db.Column(db.String(100))
    made_in = db.Column(db.String(100))
    model = db.Column(db.String(100))
    image_file = db.Column(db.String(255))

    connectivity = db.relationship('Connectivity', backref='product', uselist=False)
    body = db.relationship('Body', backref='product', uselist=False)
    display = db.relationship('Display', backref='product', uselist=False)
    back_camera = db.relationship('BackCamera', backref='product', uselist=False)
    front_camera = db.relationship('FrontCamera', backref='product', uselist=False)
    battery = db.relationship('Battery', backref='product', uselist=False)
    performance = db.relationship('Performance', backref='product', uselist=False)
    storage = db.relationship('Storage', backref='product', uselist=False)
    sound = db.relationship('Sound', backref='product', uselist=False)
    security = db.relationship('Security', backref='product', uselist=False)
    others = db.relationship('Others', backref='product', uselist=False)

class Connectivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    network = db.Column(db.String(100))
    sim = db.Column(db.String(100))
    wlan = db.Column(db.String(100))
    bluetooth = db.Column(db.String(100))
    gps = db.Column(db.String(100))
    radio = db.Column(db.String(100))
    usb = db.Column(db.String(100))
    otg = db.Column(db.Boolean, default=False)
    usb_type_c = db.Column(db.Boolean, default=False)
    nfc = db.Column(db.Boolean, default=False)

class Body(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    style = db.Column(db.String(100))
    material = db.Column(db.String(100))
    water_resistance = db.Column(db.String(100))
    dimensions = db.Column(db.String(100))
    weight = db.Column(db.String(100))

class Display(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    size = db.Column(db.String(100))
    resolution = db.Column(db.String(100))
    technology = db.Column(db.String(100))
    protection = db.Column(db.String(100))
    features = db.Column(db.String(100))

class BackCamera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    resolution = db.Column(db.String(100))
    features = db.Column(db.String(100))
    video_recording = db.Column(db.String(100))

class FrontCamera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    resolution = db.Column(db.String(100))
    features = db.Column(db.String(100))
    video_recording = db.Column(db.String(100))

class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    type_capacity = db.Column(db.String(100))
    fast_charging = db.Column(db.String(100))

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    operating_system = db.Column(db.String(100))
    chipset = db.Column(db.String(100))
    processor = db.Column(db.String(100))
    speed = db.Column(db.String(100))
    gpu = db.Column(db.String(100))

class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    ram = db.Column(db.String(100))
    rom = db.Column(db.String(100))
    microsd_slot = db.Column(db.String(100))

class Sound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    jack_3_5mm = db.Column(db.String(100))
    features = db.Column(db.String(100))

class Security(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    fingerprint = db.Column(db.String(100))
    face_unlock = db.Column(db.String(100))

class Others(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    notification_light = db.Column(db.String(100))
    sensors = db.Column(db.String(100))

# END PRODUCT MODEL 