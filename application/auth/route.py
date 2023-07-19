from flask import Blueprint,render_template, redirect, url_for,flash
from application.auth.forms import RegistrationForm,LoginForm
from application.models import User
from application import bcrypt,db

auth = Blueprint('auth', __name__)


@auth.route('/signup/', methods=['GET', 'POST'])
def signUp():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if email already exists
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            form.email.errors.append('Email already exists.')
            return render_template('auth/sign-up.html', form=form)

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        flash('successfully sign-up','info')
        return redirect(url_for('auth.login'))  # Redirect to the login page


    return render_template('auth/sign-up.html', form=form)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Check if user with the provided email exists
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('auth.login'))

        # Check if password is correct
        if not bcrypt.check_password_hash(user.password, form.password.data):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('auth.login'))

        # User is authenticated, perform login
        # Add your login logic here, such as setting session variables or creating a login session

        flash('Logged in successfully!', 'success')
        return redirect(url_for('public.index'))

    return render_template('auth/sign-in.html',form=form)

