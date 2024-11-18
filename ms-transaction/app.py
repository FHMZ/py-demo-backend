from controllers.setup_rest_controller import setup_rest_controller
from flask import Flask, jsonify
from rabbitmq import RabbitMQ

app = Flask(__name__)
app.register_blueprint(setup_rest_controller)


@app.errorhandler(Exception)
def error_handler(e):
    if (hasattr(e, 'code') and e.code != None):
        return '', e.code
    else:
        return '', 500


if __name__ == "__main__":
    channel = RabbitMQ().get_channel()
    channel.queue_declare(
        queue='setup_add_account', durable=True)
    channel.queue_bind(
        queue='setup_add_account',
        exchange='amq.topic',
        routing_key='*.setup.add_account.*')
    app.run(host="0.0.0.0", port=5000, debug=True)
