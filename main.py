# -*- coding: utf-8 -*-
import pprint

from src.api import HeadHunterAPI, SuperJobAPI
from src.save_file import JSONSaver
from src.utils import (
    read_file,
    filter_vacancies,
    sort_vacancies,
    create_list_dict_hh,
    create_list_dict_sj,
    get_top_vacancies,
)
from src.working_with_vacancies import Vacancy

# Создание экземпляра класса для работы с API сайтов вакасиями
hh_api = HeadHunterAPI("Python")
sj_api = SuperJobAPI("Python")

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies()
sj_vacancies = sj_api.get_vacancies()

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy(
    "Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет..."
)

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver("save_vacancy.json")
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy.to_dict())


def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос для вакансии: ")

    # формируем json ответ
    headhunter_vacancies = HeadHunterAPI(search_query).get_vacancies()
    superjob_vacancies = SuperJobAPI(search_query).get_vacancies()

    # Создание списка экземпляров класса из API запроса
    list_vacancies_hh = create_list_dict_hh(headhunter_vacancies)
    list_vacancies_sj = create_list_dict_sj(superjob_vacancies)

    # добавление вакансий в файл JSON
    json_saver.add_vacancy(list_vacancies_hh)
    json_saver.add_vacancy(list_vacancies_sj)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # считывание всех вакансий
    all_vacancies = read_file(json_saver.path)

    # фильтруем по ключевым словам
    filtered_vacancies = filter_vacancies(all_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    # сортировка вакансий по наименованию
    sorted_vacancies = sort_vacancies(filtered_vacancies)

    # выводим топ N вакансий по зарплате
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    pprint.pprint(top_vacancies)


if __name__ == "__main__":
    user_interaction()
