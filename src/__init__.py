from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("src.config.Config")

    # Import and register blueprints from controllers
    from .controllers.demo_controller import controller
    app.register_blueprint(controller)

    return app
