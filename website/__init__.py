from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .views import home_page
    from .auth import auth
    app.register_blueprint(home_page, url_prefix="")
    app.register_blueprint(auth, url_prefix="")
    # from ..models.engine import db
    
    return app

def create_database(app):
    pass



