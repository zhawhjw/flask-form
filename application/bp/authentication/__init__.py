from flask import Blueprint, render_template, redirect, url_for, flash

from application.database import User, db
from application.bp.authentication.forms import RegisterForm

authentication = Blueprint('authentication', __name__, template_folder='templates')
@authentication.route('/dashboard')
def dashboard():
    # user_records = User.all()

    return render_template('dashboard.html')

@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    return


