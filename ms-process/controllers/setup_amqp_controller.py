from util import SingletonClass
from components.setup_component import SetupComponent
from services.setup_service import SetupService
import json


class SetupAmqpController(SingletonClass):
    def setup_add_account_callback(self, channel, method, properties, body):
        body2 = json.loads(body)
        payload = SetupComponent().add_account_from_amqp(body2.get('trx_payload'))
        response = SetupService().add_account(payload)
        trx_id = body2.get('trx_id')
        channel.basic_publish(
            exchange='amq.topic',
            routing_key=f"complete.{trx_id}",
            body=json.dumps({
                "trx_id": trx_id,
                "prx_payload": payload,
                "prx_channel": "REST",
                "prx_response": json.dumps(response)
            }))
        channel.basic_ack(delivery_tag=method.delivery_tag)
