from util import SingletonClass
import requests


class SetupRestService(SingletonClass):
    def add_account(self, payload):
        response = requests.post(
            "https://webhook.site/03b4fe0c-02f4-4841-ba79-5ab3857976ab",
            json=payload)
        return {'status_code': response.status_code, 'text': response.text}
