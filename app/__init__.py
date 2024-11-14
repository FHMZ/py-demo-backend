from flask import Flask, jsonify

from app.controllers.setup_controller import setup_controller_bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(setup_controller_bp)

    # Register Error Handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    from werkzeug.exceptions import HTTPException

    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            # Return error as JSON for HTTP errors
            return jsonify(error=str(e)), e.code
        # For non-HTTP exceptions, return 500 error
        return jsonify(error="Internal server error"), 500
