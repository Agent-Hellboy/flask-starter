import re

from flask import render_template, request, redirect, url_for, session, flash, Blueprint
from flask_login import login_required, login_user, logout_user, current_user


from .extension import db
from .models import User

main = Blueprint("main", __name__)


@main.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for("main.home"))
            else:
                flash("username or password incorrect")
    return render_template("login.html", msg=msg)


@main.route("/logout")
def logout():
    # Remove session data, this will log the user out
    logout_user()
    # Redirect to login page
    return redirect(url_for("main.login"))


@main.route("/register", methods=["GET", "POST"])
def register():
    # Output message if something goes wrong...
    msg = ""
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        # Create variables for easy access
        username = request.form["username"]
        password = request.form["password"]
        # Check if account exists in DB
        account = User.query.filter_by(username=username).first()
        # If account exists show error and validation checks
        if account:
            msg = "Account already exists!"
        elif not re.match(r"[A-Za-z0-9]+", username):
            msg = "Username must contain only characters and numbers!"
        elif not username or not password:
            msg = "Please fill out the form!"
        else:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            msg = "You have successfully registered!"
            return redirect(url_for("main.login"))
    return render_template("register.html", msg=msg)


@main.route("/")
def home():
    # Check if user is loggedin
    if "_user_id" in session:
        # User is loggedin show them the home page
        return render_template(
            "home.html", username=User.query.filter_by(id=session["_user_id"]).first()
        )
    # User is not loggedin redirect to login page
    return redirect(url_for("main.login"))


@main.route("/profile")
@login_required
def profile():
    # Check if user is loggedin
    if current_user.is_authenticated:
        # We need all the account info for the user so we can display it on the profile page

        # Show the profile page with account info
        return render_template(
            "profile.html", account=User.query.filter_by(id=session["_user_id"]).first()
        )
    # User is not loggedin redirect to login page
    return redirect(url_for("main.login"))
