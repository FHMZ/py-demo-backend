from flask import Blueprint, jsonify

setup_controller = Blueprint("controller", __name__)


@setup_controller.route('/api/setup/add_account', methods=["POST"])
def get_setup():
    return jsonify({}), 200
