from flask import Blueprint, render_template, redirect, url_for, flash

from application.database import User, db
from application.bp.authentication.forms import RegisterForm

authentication = Blueprint('authentication', __name__, template_folder='templates')


@authentication.route('/users')
def users():
    user_records = User.all()
    return render_template('users.html', users=user_records)


@authentication.route('/dashboard')
def dashboard():
    # user_records = User.all()
    return render_template('dashboard.html')


@authentication.route('/users/<user_id>')
def user_by_id(user_id):
    user = User.find_user_by_id(user_id)
    return render_template('user.html', user=user)

@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.find_user_by_email(form.email.data)
        if user is None:
            user = User.create(form.email.data, form.password.data)
            user.save()
            print(user.id)
            return redirect(url_for('authentication.dashboard', name=user.email))
        else:
            flash("Already Registered!")

    return render_template('registration.html', form=form)




