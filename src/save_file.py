import json
from abc import ABC, abstractmethod

from config import ROOT_PATH
from src.utils import read_file, record_in_file
from src.working_with_vacancies import Vacancy


class Saver(ABC):
    def __init__(self, path: str):
        self.path = ROOT_PATH.joinpath(path)
        with open(self.path, "w") as f:
            json.dump([], f)

    @abstractmethod
    def add_vacancy(self, vacancies: list[Vacancy] | Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criterions: dict) -> list[dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, criterions: dict) -> None:
        pass


class JSONSaver(Saver):
    def add_vacancy(self, vacancies: list[Vacancy] | Vacancy) -> None:
        """Метод добавления вакансий в файл JSON"""
        if type(vacancies) is not list:
            data_json = vacancies.to_dict()
            old_file = read_file(self.path)
            old_file.append(data_json)
            record_in_file(self.path, old_file)

        else:
            data_json = [vacancy.to_dict() for vacancy in vacancies]
            old_file = read_file(self.path)

            old_file.extend(data_json)
            record_in_file(self.path, old_file)

    def get_vacancies(self, criterions: dict) -> list[dict]:
        """Метод получения  вакансий из  файла JSON по критериям или критерию"""

        all_vacancies = read_file(self.path)

        result_vacancies = []
        if len(criterions.keys()) == 1:
            for key, value in criterions.items():
                for vacancy in all_vacancies:
                    if vacancy[key] == value:
                        result_vacancies.append(vacancy)

        elif len(criterions.keys()) > 1:
            for vacancy in all_vacancies:
                if all(vacancy.get(key) == value for key, value in criterions.items()):
                    result_vacancies.append(vacancy)

        return result_vacancies

    def delete_vacancy(self, criterions=None) -> None:
        """Метод удаления вакансий из  файла JSON по критериям
        или критерию(указать нужно в критериях что нужно оставить)"""

        result_vacancies = self.get_vacancies(criterions)
        record_in_file(self.path, result_vacancies)
