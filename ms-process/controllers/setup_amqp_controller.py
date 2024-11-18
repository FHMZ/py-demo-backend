from util import SingletonClass
from components.setup_component import SetupComponent
from services.setup_service import SetupService
import json


class SetupAmqpController(SingletonClass):
    def setup_add_account_callback(self, channel, method, properties, body):
        payload = SetupComponent().add_account_from_amqp(json.loads(body))
        response = SetupService().add_account(payload)
        channel.basic_ack(delivery_tag=method.delivery_tag)
        channel.basic_publish(
            exchange='amq.topic',
            routing_key=f"complete.{payload.trx_id}",
            body=json.dumps(response))
