from util import SingletonClass


class SetupComponent(SingletonClass):
    def add_account_from_amqp(self, message):
        return message.get('trx_payload')
