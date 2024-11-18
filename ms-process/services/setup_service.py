from util import SingletonClass
import requests


class SetupService(SingletonClass):
    def add_account(self, payload):
        response = requests.post(
            "https://webhook.site/03b4fe0c-02f4-4841-ba79-5ab3857976ab",
            json=payload)
        print(str(response))
        return {'protocol': '123'}
