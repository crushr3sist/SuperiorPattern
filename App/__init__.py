from flask import Flask
from flask_login import LoginManager

from App.extension_globals.database import db


class SuperiorPattern(Flask):
    def __init__(
        self, import_name: str, template_folder: None = None, root_path: None = None
    ):
        super().__init__(import_name, template_folder, root_path)
        with self.app_context():
            self.import_config()
            self.import_db()
            self.import_cookies()
            self.import_blueprints()

    def import_db(self):
        db.init_app(self)
        from App.components.index.models import Todo
        from App.components.Authentication import models

        db.create_all()

    def import_cookies(self):
        from App.extension_globals.cookies import login_manager

        login_manager.init_app(self)
        from App.components.Authentication.models import User

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(user_id)

        login_manager.login_view = "authentication_view.login"

    def import_config(self):
        return self.config.from_object("App.config.Config")

    def import_blueprints(self):
        from App.components.index.views import index_view
        from App.components.Authentication.views import authentication_view

        self.register_blueprint(index_view)
        self.register_blueprint(authentication_view)


app = SuperiorPattern(__name__)
