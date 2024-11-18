from flask import Blueprint, jsonify, request
from util import SingletonClass
from validations.setup_validation import SetupValidation
from rabbitmq import RabbitMQ
import uuid
import json

setup_controller = Blueprint("controller", __name__)


class SetupController(SingletonClass):
    @setup_controller.route('/api/setup/add_account', methods=["POST"])
    def add_account():
        SetupValidation().validate_add_account(request)
        id = uuid.uuid4()
        trx_id = f"setup.add_account.{id}"
        body = json.dumps({
            "trx_id": trx_id,
            "fi_id": 1,
            "client_id": 2,
            "trx_payload": request.json,
            "trx_channel": "REST"})
        channel = RabbitMQ().get_channel()
        channel.basic_publish(
            exchange='amq.topic',
            routing_key=f"process.setup.add_account.{id}",
            body=body)
        return jsonify({"trx_id": trx_id}), 200
