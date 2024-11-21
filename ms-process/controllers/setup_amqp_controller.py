from util import SingletonClass
from components.setup_component import SetupComponent
from services.setup_celero_core_lib_service import SetupCeleroCoreLibService
import json


class SetupAmqpController(SingletonClass):
    def setup_add_account_callback(self, channel, method, properties, body):
        message = json.loads(body)
        request_payload = SetupComponent().add_account_from_amqp(message)
        response = SetupCeleroCoreLibService().add_account(request_payload)
        trx_id = message.get('trx_id')
        channel.basic_publish(
            exchange='amq.topic',
            routing_key=f"complete.{trx_id}",
            body=json.dumps({
                "trx_id": trx_id,
                "prx_payload": request_payload,
                "prx_channel": "REST",
                "prx_response": json.dumps(response)
            }))
        channel.basic_ack(delivery_tag=method.delivery_tag)
