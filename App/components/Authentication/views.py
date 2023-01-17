from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_login import login_user, current_user, logout_user, login_required

authentication_view = Blueprint(
    "authentication_view", __name__, template_folder="templates", url_prefix="/auth"
)

from ...extension_globals.database import db
from .models import User


@authentication_view.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        if User.query.filter_by(username=username).first():
            return (
                "user already exists, please login <button href='/auth/login'></button>"
            )
        user = User(username, password, name)
        db.session.add(user)
        db.session.commit()

    return render_template("register.html")


@authentication_view.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if User.query.filter_by(username=username).first():
            user = User.query.filter_by(username=username).first()

            if user.check_password(password):
                login_user(user, remember=True, force=True)
                print("user was authenticated correctly")
                return redirect(url_for("authentication_view.user"))
    return render_template("login.html")


@authentication_view.route("/me", methods=["GET"])
def user():
    if current_user.is_authenticated:
        return f"username: {current_user.username} name: {current_user.name}"
    return redirect(url_for("authentication_view.login"))


@authentication_view.route("/logout", methods=["GET"])
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for("authentication_view.login"))
