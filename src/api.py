import os
from abc import ABC, abstractmethod
from typing import Any

import requests
from dotenv import load_dotenv

from config import HH_URL, SP_URL

load_dotenv()


class API(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self):
        """Абстрактный метод для работы с API"""
        pass


class HeadHunterAPI(API):
    """Класс для работы с API с сайта HeadHunter"""

    def __init__(self, name_vacancies: str):
        self.name_vacancies = name_vacancies
        self.params: dict = {
            "text": self.name_vacancies,  # Текст фильтра.
            "area": 1,  # Поиск ощуществляется по вакансиям города Москва
            "page": 0,  # Индекс страницы поиска на HH
            "per_page": 10,  # Кол-во вакансий на 1 странице
        }

    def get_vacancies(self) -> Any:
        """Метод получения файла json с помощью API- запроса"""
        response = requests.get(HH_URL, params=self.params).json()  # Посылаем запрос к API

        return response


class SuperJobAPI(API):
    """Класс для работы с API с сайта SuperJob"""

    def __init__(self, name_vacancies: str):
        self.name_vacancies = name_vacancies
        self.params: dict = {"keyword": name_vacancies, "count": 100}
        self.headers: dict = {"X-Api-App-Id": os.getenv("SJ_key")}

    def get_vacancies(self) -> Any:
        """Метод получения файла json с помощью API- запроса"""
        response = requests.get(SP_URL, headers=self.headers, params=self.params).json()  # Посылаем запрос к API

        return response
