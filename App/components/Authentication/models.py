from ...extension_globals.database import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = "users_table"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    hashed_password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)

    is_authenticated: str
    is_active: str
    is_anonymous: str

    def __init__(self, username, password, name):
        self.username = username
        self.hashed_password = generate_password_hash(password)
        self.name = name

    def is_active(self) -> bool:
        """
        Check if user is active.
        """
        return self.is_active

    def check_password(self, password) -> bool:
        """
        Check if user's password is correct.
        """
        return check_password_hash(self.hashed_password, password)

    def get_id(self) -> str:
        """
        Get the user's id.
        """
        return self.id

    def is_authenticated(self) -> bool:
        """
        Check if user is authenticated.
        """
        return self.authenticated

    def is_anonymous(self) -> bool:
        """
        Check if user is anonymous.
        """
        return self.is_anonymous

    @property
    def identity(self) -> str:
        """
        Get the user's identity.
        """
        return self.id

    @property
    def rolenames(self) -> list:
        """
        Get the user's roles.
        """
        try:
            return self.roles.split(",")
        except Exception:
            return []

    @property
    def password(self) -> str:
        """
        Get the user's password.
        """
        return self.hashed_password

    @classmethod
    def lookup(cls, username) -> "User":
        """
        Lookup a user by username.
        """

        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id) -> "User":
        """
        Lookup a user by id.
        """

        return cls.query.get(id)

    def is_valid(self) -> bool:
        """
        Check if user is valid.
        """
        return self.is_active
