import requests
import json

from src.abc_cls import Vacancies


class SuperJobAPI(Vacancies):

    def get_vacancies(self, *answer):
        headers = {
                "X-Api-App-Id":
                'v3.r.114141450.67b5bbb954d345174b7c434bcd0f00a911c24e67.efd32f9c45464631a84c6bbad1015fc450bdff5f'
                   }
        params = {
            "keyword": answer,
        }
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        data = response.content.decode()
        vacant = json.loads(data)
        return vacant
