from controllers.setup_controller import setup_controller
from flask import Flask, jsonify

app = Flask(__name__)
app.register_blueprint(setup_controller)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
