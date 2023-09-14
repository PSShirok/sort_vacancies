
import json
from abc import ABC, abstractmethod


class FileAbsract(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class Vacancy:
    def __init__(self, name, employer, salary, requirements, responsibility, url):
        self.name = name
        self.employer = employer
        self.salary = salary
        self.requirements = requirements
        self.responsibility = responsibility
        self.url = url

    def __dict__(self):
        """
        метод для добавления данных экземпляров класса в словарь
        """
        return{"name": self.name,
               "employer": self.employer,
               "salary": self.salary,
               "requirements": self.requirements,
               "responsibility": self.responsibility,
               "url": self.url}

    def __str__(self):
        return self.name

    @staticmethod
    def compare_salary():
        """
        метод для сортировки по зар.плате и вывода заданного
        пользователем коли-ва вакансий
        """
        with open('vacancy.json', 'r', encoding='utf-8') as outfile:
            vacancies_data = json.load(outfile)
            for vacancy in vacancies_data:
                if vacancy['salary'] is None:
                    vacancy['salary'] = 0
            new_list = sorted(vacancies_data, key=lambda d: d['salary'], reverse=True)
            return new_list


class Filework(FileAbsract):

    def __init__(self):
        pass

    @staticmethod
    def add_vacancy(file):
        """
        метод для добавления вакнсий в файл
        """
        with open('vacancy.json', 'r', encoding='utf-8') as outfile:
            content = json.load(outfile)
        content.append(file.__dict__())
        with open('vacancy.json', 'w', encoding='utf-8') as outfile:
            json.dump(content, outfile, ensure_ascii=False, indent=6)

    @staticmethod
    def del_vacancy():
        """
        метод для удаления вакансий из файла
        """
        with open('vacancy.json', "w", encoding='utf-8') as outfile:
            content = []
            json.dump(content, outfile)


def created_hh_vacancy(vacant):
    """
    функция для создания экземпляров класса с HeadHunter
    """
    for vacancy in vacant['items']:
        name = vacancy['name']
        employer = vacancy['employer']['name']
        if vacancy['salary']:
            salary = vacancy['salary']['from']
        else:
            salary = 0
        requirements = vacancy['snippet']['requirement']
        responsibility = vacancy['snippet']['responsibility']
        url = vacancy['alternate_url']
        vacancy_for_file = Vacancy(name, employer, salary, requirements, responsibility, url)
        Filework.add_vacancy(vacancy_for_file)


def created_sj_vacancy(vacant):
    """
    функция для создания экземпляров класса с Superjob
    """
    for vacancy in vacant['objects']:
        try:
            name = vacancy['profession']
            employer = vacancy['client']['title']
            salary = vacancy['payment_to']
            requirements = vacancy['candidat']
            responsibility = vacancy['vacancyRichText']
            url = vacancy['link']
        except KeyError:
            pass
        else:
            vacancy_for_file = Vacancy(name, employer, salary, requirements, responsibility, url)
            Filework.add_vacancy(vacancy_for_file)
