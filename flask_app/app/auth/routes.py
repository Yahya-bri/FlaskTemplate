from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from app.auth import bp
from app.extensions import db
from app.models.auth import User
from werkzeug.security import check_password_hash, generate_password_hash

@bp.route("/login")
def login():
    return render_template("auth/login.html")

@bp.route("/login", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]

    # Check if the user exists and the password is correct.
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return redirect(url_for("auth.login"))
    
    # Log in the user.
    login_user(user)
    return redirect(url_for("main.index"))

@bp.route("/signup")
def signup():
    return render_template("auth/signup.html")

@bp.route("/signup", methods=["POST"])
def signup_post():
    username = request.form["username"]
    password = request.form["password"]

    # Create a new user object and add it to the database.
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth.login"))

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))