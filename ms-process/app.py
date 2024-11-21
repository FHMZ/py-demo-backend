from rabbitmq import RabbitMQ
from controllers.setup_amqp_controller import SetupAmqpController
import logging


def setup_rabbitmq():
    channel = RabbitMQ().get_channel()
    channel.queue_declare(
        queue='setup_add_account', durable=True)
    channel.queue_declare(
        queue='logger', durable=True)
    channel.queue_bind(
        queue='setup_add_account',
        exchange='amq.topic',
        routing_key='process.setup.add_account.*')
    channel.queue_bind(
        queue='logger',
        exchange='amq.topic',
        routing_key='*.*.*.*')
    channel.basic_qos()
    channel.basic_consume(
        queue='setup_add_account',
        on_message_callback=SetupAmqpController().setup_add_account_callback)
    channel.start_consuming()


if __name__ == "__main__":
    logging.basicConfig()
    setup_rabbitmq()
