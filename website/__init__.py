from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
DB_PATH = path.join(path.dirname(__file__), DB_NAME)

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supper secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note
    
    # NOTE -> (flask_sqlalchemy) How you create the data base has changed in the new version. The commented put code is the way the tutorial dose it.

    # if not path.exists('website/' + DB_NAME):
    #     db.create_all(app=app)
    #     print('Created Database!')

    if not path.exists(DB_PATH):
        with app.app_context():
            db.create_all()
        print("Created Database!")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

    
        