import pika
import os
from util import SingletonClass
from pika.exceptions import StreamLostError


class RabbitMQ(SingletonClass):
    connection = None

    def get_channel(self, force=0):
        if force > 3:
            raise RuntimeError('FORCE>3')
        try:
            if self.connection == None or force > 0:
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
        except StreamLostError:
            return self.get_channel(force+1)
