import json
from abc import ABC, abstractmethod

from src.working_with_vacancies import Vacancy


class Saver(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criterions: dict) -> list[dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, criterions: dict) -> None:
        pass


class JSONSaver(Saver):
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:

        """Метод добавления вакансий в файл JSON"""

        data_json = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.path, encoding="utf-8") as file:
            old_file = json.load(file)
        old_file.extend(data_json)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(old_file, file)

    def get_vacancies(self, criterions: dict) -> list[dict]:

        """Метод получения  вакансий из  файла JSON по критериям или критерию"""

        with open(self.path, encoding="utf-8") as file:
            all_vacancies = json.load(file)

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
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(result_vacancies, file)
