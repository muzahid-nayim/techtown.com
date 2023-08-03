

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, BooleanField,IntegerField
from wtforms.validators import DataRequired,NumberRange

# START ADD BRAND FORM 
class AddBrandForm(FlaskForm):
    brand_name = StringField('Brand', validators=[DataRequired()])
    logo = FileField('Brand Logo') 
    submit = SubmitField('Add Brand')
# END ADD BRAND FORM 

# START EDIT BRAND FORM 
class EditBrandForm(FlaskForm):
    brand_name = StringField('Brand', validators=[DataRequired()])
    logo = FileField('Brand Logo') 
    submit = SubmitField('Update Brand')
# END EDIT BRAND FORM 

# START PRODUCT FORM 
class ProductForm(FlaskForm):
    # Product fields
    first_release = StringField('First Release', validators=[DataRequired()])
    colors = StringField('Colors', validators=[DataRequired()])
    manufactured_by = StringField('Manufactured by', validators=[DataRequired()])
    made_in = StringField('Made in', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0, max=99999999)])
    model = StringField('Model', validators=[DataRequired()])
    image = FileField('Product Image')
    
    # Connectivity fields
    network = StringField('Network', validators=[DataRequired()])
    sim = StringField('SIM', validators=[DataRequired()])
    wlan = StringField('WLAN', validators=[DataRequired()])
    bluetooth = StringField('Bluetooth', validators=[DataRequired()])
    gps = StringField('GPS', validators=[DataRequired()])
    radio = StringField('Radio', validators=[DataRequired()])
    usb = StringField('USB', validators=[DataRequired()])
    otg = BooleanField('OTG')
    usb_type_c = BooleanField('USB Type-C')
    nfc = BooleanField('NFC')

    # Body fields
    style = StringField('Style', validators=[DataRequired()])
    material = StringField('Material', validators=[DataRequired()])
    water_resistance = StringField('Water Resistance', validators=[DataRequired()])
    dimensions = StringField('Dimensions', validators=[DataRequired()])
    weight = StringField('Weight', validators=[DataRequired()])

    # Display fields
    size = StringField('Size', validators=[DataRequired()])
    resolution = StringField(' Display Resolution', validators=[DataRequired()])
    technology = StringField('Technology', validators=[DataRequired()])
    protection = StringField('Protection', validators=[DataRequired()])
    features_display = StringField('Features', validators=[DataRequired()])

    # Back Camera fields
    resolution_back = StringField(' Back Camera Resolution', validators=[DataRequired()])
    features_back = StringField('Back Camera Features', validators=[DataRequired()])
    video_recording_back = StringField('Video Recording', validators=[DataRequired()])

    # Front Camera fields
    resolution_front = StringField('Front Camera Resolution', validators=[DataRequired()])
    features_front = StringField('Front Camera Features', validators=[DataRequired()])
    video_recording_front = StringField('Video Recording', validators=[DataRequired()])

    # Battery fields
    type_capacity = StringField('Type and Capacity', validators=[DataRequired()])
    fast_charging = StringField('Fast Charging', validators=[DataRequired()])

    # Performance fields
    os = StringField('Operating System', validators=[DataRequired()])
    chipset = StringField('Chipset', validators=[DataRequired()])
    processor = StringField('Processor', validators=[DataRequired()])
    speed = StringField('Speed', validators=[DataRequired()])
    gpu = StringField('GPU', validators=[DataRequired()])

    # Storage fields
    ram = StringField('RAM', validators=[DataRequired()])
    rom = StringField('ROM', validators=[DataRequired()])
    microsd_slot = StringField('MicroSD Slot', validators=[DataRequired()])

    # Sound fields
    mm_jack = StringField('3.5mm Jack', validators=[DataRequired()])
    features_sound = StringField('Features', validators=[DataRequired()])

    # Security fields
    fingerprint = StringField('Fingerprint', validators=[DataRequired()])
    face_unlock = StringField('Face Unlock', validators=[DataRequired()])

    # Others fields
    notification_light = StringField('Notification Light', validators=[DataRequired()])
    sensors = StringField('Sensors', validators=[DataRequired()])

    submit = SubmitField('Add Product')
# END PRODUCT FORM 

