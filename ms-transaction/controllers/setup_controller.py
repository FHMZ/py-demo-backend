from flask import Blueprint, jsonify, request
from util import SingletonClass
from rabbitmq import RabbitMQ
import uuid
import json

setup_controller = Blueprint("controller", __name__)


class SetupController(SingletonClass):
    @setup_controller.route('/api/setup/add_account', methods=["POST"])
    def add_account():
        id = uuid.uuid4()
        trx_id = f"setup.add_account.{id}"
        channel = RabbitMQ().get_channel()
        channel.queue_declare(
            queue='hello')
        body = json.dumps({"trx_id": trx_id, "fi_id": 1,
                          "client_id": 2, "trx_payload": request.json, "trx_channel": "REST"})
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body=body)
        return jsonify({"trx_id": trx_id}), 200
