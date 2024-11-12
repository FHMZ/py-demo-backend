from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object("config.Config")

from src.controllers.setup_controller import setup_controller
app.register_blueprint(setup_controller)

@app.errorhandler(Exception)
def error_handler(e):
    if (hasattr(e, 'code') and e.code != None):
        return '', e.code
    else:
        return '', 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
