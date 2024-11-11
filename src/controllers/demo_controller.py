from flask import Blueprint, jsonify, request
from src.components.demo_component import process_demo_response_data

controller = Blueprint("controller", __name__)

@controller.route("/api/demo", methods=["GET"])
def get_demo():
    data = process_demo_response_data()
    return jsonify(data), 200
