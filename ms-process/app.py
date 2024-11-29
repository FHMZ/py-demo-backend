from rabbitmq import RabbitMQ
from controllers.company_amqp_controller import CompanyAmqpController
import logging


def setup_rabbitmq():
    channel = RabbitMQ().get_channel()
    channel.queue_declare(
        queue='company_create_company', durable=True)
    channel.queue_declare(
        queue='logger', durable=True)
    channel.queue_bind(
        queue='company_create_company',
        exchange='amq.topic',
        routing_key='process.company.create_company.*')
    channel.queue_bind(
        queue='logger',
        exchange='amq.topic',
        routing_key='*.*.*.*')
    channel.basic_qos()
    channel.basic_consume(
        queue='company_create_company',
        on_message_callback=CompanyAmqpController().create_company_callback)
    channel.start_consuming()


if __name__ == "__main__":
    logging.basicConfig()
    setup_rabbitmq()
