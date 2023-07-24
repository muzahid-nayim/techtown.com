import os
import secrets
from flask import current_app
from werkzeug.utils import secure_filename

def save_brand_image(image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image.filename)
    image_filename = random_hex + f_ext
    image_path = os.path.join(current_app.root_path, 'static', 'brand_logos', image_filename)

    image.save(image_path)

    return image_filename