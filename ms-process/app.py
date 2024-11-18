from rabbitmq import RabbitMQ
from controllers.setup_amqp_controller import SetupAmqpController


def setup_add_account_callback(channel, method, properties, body):
    print(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
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
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='setup_add_account',
        on_message_callback=SetupAmqpController().setup_add_account_callback)
    channel.start_consuming()
