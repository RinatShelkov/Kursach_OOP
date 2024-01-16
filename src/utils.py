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
