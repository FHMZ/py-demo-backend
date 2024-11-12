from flask import Blueprint, jsonify
from src.components.setup_component import process_get_setup, process_post_setup

setup_controller = Blueprint("controller", __name__)

@setup_controller.route('/api/setup', methods=["GET"])
def get_setup():
    return jsonify(process_get_setup()), 200

@setup_controller.route('/api/setup', methods=["POST"])
def post_setup():
    return jsonify(process_post_setup({"id": 123, "settings": "xyz"})), 200
