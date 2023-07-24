# application/decorators.py

from functools import wraps
from flask import render_template
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.user_role == 'admin':
            return f(*args, **kwargs)
        else:
            return render_template('error/403.html'), 403  # Return a 403 Forbidden error
    return decorated_function