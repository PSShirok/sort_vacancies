import requests
import json

from src.abc_cls import Vacancies


class HeadHunterAPI(Vacancies):
    def get_vacancies(self, *answer):
        params = {
            "text": answer
        }
        req = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = req.content.decode()
        vacant = json.loads(data)
        return vacant
