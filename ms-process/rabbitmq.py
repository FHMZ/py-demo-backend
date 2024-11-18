import pika
import os
from util import SingletonClass

class RabbitMQ(SingletonClass):
    connection = None

    def get_channel(self):
        if self.connection == None:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=os.getenv('RABBITMQ_HOST'),
                    credentials=pika.credentials.PlainCredentials(
                        os.getenv('RABBITMQ_USER'),
                        os.getenv('RABBITMQ_PASS'))
                )
            )
        channel = self.connection.channel()
        return channel
