import json

from src.functions import Filework, created_hh_vacancy, Vacancy, created_sj_vacancy
from src.hh_api import HeadHunterAPI
from src.sj_api import SuperJobAPI

if __name__ == "__main__":

    Filework.del_vacancy()
    platform_answer = int(input("Привет, где будем искать работу (укажи цифру)?\n"
                                "1. HeadHunter\n"
                                "2. SuperJob\n"
                                "3. HeadHunter + SuperJob\n"))

    key_word = str(input("Какие вакансии интересуют?\n"
                         "И, если интересует конкретный город, напиши его тоже,\n"
                         "например 'Директор Москва'\n")).lower()

    if platform_answer == 1:
        hh = HeadHunterAPI()
        vacant = hh.get_vacancies(key_word)
        created_hh_vacancy(vacant)
    elif platform_answer == 2:
        sj = SuperJobAPI()
        vacant = sj.get_vacancies(key_word)
        created_sj_vacancy(vacant)
    elif platform_answer == 3:
        sj = SuperJobAPI()
        hh = HeadHunterAPI()
        vacant_hh = hh.get_vacancies(key_word)
        vacant_hh_sj = sj.get_vacancies(key_word)
        created_hh_vacancy(vacant_hh)
        created_sj_vacancy(vacant_hh_sj)
    else:
        print("Если хочешь чтобы работало, напиши 1,2 или 3 при следующем запуске")
        exit()

    top_vacan = int(input("Какие вакансии будем смотреть?\n"
                          "1. Показать все найденные\n"
                          "2. Вывести ТОП высокооплачиваемых\n"))
    if top_vacan == 2:
        count_top = int(input("Сколько вакансий показать?\n"))
        top_vacancies = Vacancy.compare_salary()
        for i in range(count_top):
            print(top_vacancies[i]['name'], top_vacancies[i]['employer'],
                  top_vacancies[i]['salary'], top_vacancies[i]['url'])

    elif top_vacan == 1:
        with open('vacancy.json', 'r', encoding='utf-8') as outfile:
            vacancies_data = json.load(outfile)
            for vacancy in vacancies_data:
                print(vacancy['name'], vacancy['employer'],
                      vacancy['salary'], vacancy['url'])

    print("УДАЧИ В ПОИСКЕ!!!")
