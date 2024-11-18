from util import SingletonClass


class SetupComponent(SingletonClass):
    def add_account_from_amqp(self, payload):
        return payload
