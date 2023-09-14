from abc import ABC, abstractmethod


class Vacancies(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass