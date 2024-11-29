from util import SingletonClass
from components.company_component import CompanyComponent
from services.company_celero_core_lib_service import CompanyCeleroCoreLibService
from services.company_rest_service import CompanyRestService
import json


class CompanyAmqpController(SingletonClass):
    def create_company_callback(self, channel, method, properties, body):
        message = json.loads(body)
        request_payload = CompanyComponent().create_company_from_amqp(message)
        CompanyCeleroCoreLibService().create_company(request_payload)
        response = CompanyRestService().create_company(request_payload)
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
