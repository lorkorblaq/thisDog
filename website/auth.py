from flask import Blueprint, render_template, request, url_for, redirect, flash    
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegistrationForm, LoginForm
import secrets

auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")

@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('views.home'))
    return render_template("register.html", title='Register', form=form)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome {form.email.data}!', 'success')
        return redirect(url_for('views.home'))
    return render_template("login.html", title='Login',form=form)

@auth.route("/logout")
def logout():
    return render_template("index.html")


