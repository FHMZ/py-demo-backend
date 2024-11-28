from util import SingletonClass
import requests


class SetupRestService(SingletonClass):
    def add_account(self, payload):
        response = requests.post(
            "https://webhook.site/26661c98-1aec-4b18-8362-e9acfb88e9e1",
            json=payload)
        return {'status_code': response.status_code, 'text': response.text}
