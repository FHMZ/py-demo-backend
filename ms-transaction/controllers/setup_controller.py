from flask import Blueprint, jsonify
from util import SingletonClass
from rabbitmq import RabbitMQ

setup_controller = Blueprint("controller", __name__)


class SetupController(SingletonClass):
    @setup_controller.route('/api/setup/add_account', methods=["POST"])
    def get_setup():
        channel = RabbitMQ().get_channel()
        channel.queue_declare(
            queue='hello')
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body='Hello World!')
        return jsonify({}), 200
