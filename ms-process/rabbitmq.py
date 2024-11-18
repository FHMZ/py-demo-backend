import pika
from util import SingletonClass


class RabbitMQ(SingletonClass):
    connection = None

    def get_channel(self):
        if self.connection == None:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host='localhost',
                    credentials=pika.credentials.PlainCredentials(
                        'admin', 'celero123')
                )
            )
        channel = self.connection.channel()
        return channel
