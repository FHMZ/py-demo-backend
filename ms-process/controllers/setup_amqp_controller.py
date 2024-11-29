from util import SingletonClass
from components.setup_component import SetupComponent
from services.celero_core_lib_service import CeleroCoreLibService
import json


class SetupAmqpController(SingletonClass):
    def setup(self, channel, method, properties, body):
        message = json.loads(body)

        create_bank_request = SetupComponent().create_bank_from_amqpb(message)
        create_bank_response = CeleroCoreLibService().create_bank(create_bank_request)

        print('CREATE_BANK_REQUEST -> ', create_bank_request)

        create_company_request = SetupComponent().create_company_from_amqpb(message)
        create_company_response = CeleroCoreLibService().create_company(create_company_request)

        create_account_request = SetupComponent().create_account_from_amqpb(message)
        create_account_response = CeleroCoreLibService().create_account(create_account_request)

        create_user_request = SetupComponent().create_user_from_amqpb(message)
        create_user_response = CeleroCoreLibService().create_user(create_user_request)

        channel.basic_ack(delivery_tag=method.delivery_tag)
