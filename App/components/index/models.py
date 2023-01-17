from ...extension_globals.database import db


class Todo(db.Model):

    __tablename__ = "todo_table"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    owner_id = db.Column(db.Integer())

    def __init__(self, name, owner_id):
        self.name = name
        self.owner_id = owner_id
