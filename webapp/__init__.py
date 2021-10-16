from flask import Flask, flash, redirect, render_template, url_for
from flask_login import LoginManager, current_user, login_required
from webapp.user.forms import LoginForm
from webapp.db import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.main_page.views import blueprint as main_page_blueprint
from webapp.user_page.views import blueprint as user_page_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(main_page_blueprint)
    app.register_blueprint(user_page_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    

    return app