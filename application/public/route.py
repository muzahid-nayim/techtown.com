from flask import Blueprint,render_template
from flask_login import current_user
from application.models import Brand

public = Blueprint('public', __name__)

@public.route('/')
def index():
    brands = Brand.query.all()
    return render_template('public/home.html',current_user=current_user, brands=brands)
