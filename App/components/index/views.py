from flask import Flask, Blueprint, render_template, request
from flask_login import login_required, current_user

index_view = Blueprint(
    "index_view", __name__, template_folder="templates", url_prefix="/"
)

from ...extension_globals.database import db
from .models import Todo


@index_view.route("/index")
@login_required
def index_route():
    return "you're at the index"


@index_view.route("/todo", methods=["POST", "GET"])
@login_required
def handle_todo():
    if request.method == "POST":
        todo_name = request.form["name"]
        todo = Todo(todo_name, current_user.id)
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.filter_by(owner_id=current_user.id).all()
    return render_template("todo.html", data_fetch=todos)
