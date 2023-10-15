from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from app.auth import bp
from app.extensions import db
from app.models.auth import User

@bp.route("/login")
def login():
    return render_template("auth/login.html")

@bp.route("/login", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]

    # Check if the user exists and the password is correct.
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return redirect(url_for("auth.login"))

    # Log the user in.
    login_user(user)

    # Redirect the user to the desired page.
    return redirect(url_for("main.index"))

@bp.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("auth.login"))

# ... Add other authentication routes here, such as registration, reset password, etc.
