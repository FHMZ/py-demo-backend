from util import SingletonClass
import requests


def send_payload(payload):
    response = requests.post(
        "https://webhook.site/26661c98-1aec-4b18-8362-e9acfb88e9e1",
        json=payload)
    return {'status_code': response.status_code, 'text': response.text}


class CeleroCoreLibService(SingletonClass):
    def create_bank(self, payload):
        return send_payload(payload)

    def create_company(self, payload):
        return send_payload(payload)

    def create_account(self, payload):
        return send_payload(payload)

    def create_user(self, payload):
        return send_payload(payload)
