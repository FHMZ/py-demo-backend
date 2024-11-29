from rabbitmq import RabbitMQ
from controllers.setup_amqp_controller import SetupAmqpController


def setup_rabbitmq():
    channel = RabbitMQ().get_channel()
    channel.queue_declare(
        queue='setup', durable=True)
    channel.queue_bind(
        queue='setup',
        exchange='amq.topic',
        routing_key='process.setup.setup.*')
    channel.basic_qos()
    channel.basic_consume(
        queue='setup',
        on_message_callback=SetupAmqpController().setup)
    channel.start_consuming()


if __name__ == "__main__":
    setup_rabbitmq()
