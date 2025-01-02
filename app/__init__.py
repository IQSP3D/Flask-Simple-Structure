from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    with app.app_context():
        from . import routes  # Import routes
        return app
