from util import SingletonClass


class CompanyComponent(SingletonClass):
    def create_company_from_amqp(self, message):
        return message.get('trx_payload')
