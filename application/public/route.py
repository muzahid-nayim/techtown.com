from flask import Blueprint

public = Blueprint('public', __name__)

@public.route('/', methods=['GET'])
def index():
    return "Hello, world!"
