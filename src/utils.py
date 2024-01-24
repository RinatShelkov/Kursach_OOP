import json
import re
from typing import Any
from os import PathLike

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
            wage=dict_to_integer(vacancy["salary"]),
            description=vacancy["snippet"]["requirement"],
        )
        for vacancy in vacancies
    ]
    return all_vacancies


def sort_vacancies(vacancies: list[Vacancy] | list[dict]):
    return sorted(vacancies, key=lambda d: d["name_vacancies"], reverse=True)


def read_file(path: PathLike):
    """Функция чтения файла JSON"""
    try:
        with open(path, encoding="utf-8") as file:
            open_file = json.load(file)

    except FileNotFoundError:
        open_file = []

    return open_file


def record_in_file(path: PathLike, record_file: Any):
    """Функция записи в JSON файл"""

    with open(path, "w", encoding="utf-8") as file:
        json.dump(record_file, file)


def filter_vacancies(list_dict: list[dict], search_words: list) -> list[dict]:
    """Функция фильтрации по ключевым словам"""

    filtered_list = []
    for word in search_words:
        for dictionary in list_dict:
            for key, value in dictionary.items():
                if key == "name_vacancies" or key == "description":
                    if re.search(word, Vacancy.validate_salary(value), flags=re.IGNORECASE):
                        filtered_list.append(dictionary)
                        break
    return filtered_list


def dict_to_integer(dictionary: dict | None) -> int:
    """Функция записи заработной платы для HeadHunter из словаря в число"""

    if dictionary is None:
        return 0
    for key, value in dictionary.items():
        if key == "from" and value is not None:
            if value > 0:
                return value
        if key == "to" and value is not None:
            if value > 0:
                return value


def get_top_vacancies(list_dict: list[dict], top_n):
    result = sorted(list_dict, key=lambda d: d["wage"], reverse=True)

    return result[:top_n]
