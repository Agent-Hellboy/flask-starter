from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from .extension import db
from .forms import LoginForm, RegistrationForm
from .models import User

main = Blueprint("main", __name__)


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("main.home"))
        flash("Invalid username or password")
    return render_template("login.html", form=form)


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))


@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("Account already exists")
            return render_template("register.html", form=form)

        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have successfully registered")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)


@main.route("/")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for("main.login"))
    return render_template("home.html", username=current_user.username)


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", account=current_user)
