import json
from typing import Any

from src.working_with_vacancies import Vacancy


def create_list_dict_sj(vacancies: list[dict]) -> list[Vacancy]:
    """Создание списка экземпляров класса из API запроса - SuperJobAPI (json-Ответа)"""

    all_vacancies = [
        Vacancy(
            name_vacancies=vacancy["profession"],
            url_vacancies=vacancy["link"],
            wage=vacancy["payment_from"],
            description=vacancy["candidat"],
        )
        for vacancy in vacancies
    ]
    return all_vacancies


def create_list_dict_hh(vacancies: list[dict]) -> list[Vacancy]:
    """Создание списка экземпляров класса из API запроса - HeadHunterAPI(API) (json-Ответа)"""

    all_vacancies = [
        Vacancy(
            name_vacancies=vacancy["name"],
            url_vacancies=vacancy["alternate_url"],
            wage=vacancy["salary"],
            description=vacancy["snippet"]["requirement"],
        )
        for vacancy in vacancies
    ]
    return all_vacancies


def sort_vacancies_by_salary(vacancies: list[Vacancy]):
    return sorted(vacancies, reverse=True)


def read_file(path: str):
    """Функция чтения файла JSON"""
    try:
        with open(path, encoding="utf-8") as file:
            open_file = json.load(file)

    except FileNotFoundError:
        open_file = []

    return open_file


def record_in_file(path: str, record_file: Any):
    """Функция записи в JSON файл"""

    with open(path, "w", encoding="utf-8") as file:
        json.dump(record_file, file)
