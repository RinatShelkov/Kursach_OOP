class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, name_vacancies, url_vacancies, wage, description):
        self.name_vacancies = name_vacancies
        self.url_vacancies = url_vacancies
        self.wage = wage
        self.description = description

    @staticmethod
    def validate_salary(salary):

        """Метод валидации данных(проверка на None из апи запроса HeadHunter)"""

        if salary is None:
            return 0
        return salary

    def __eq__(self, other):
        return int(self.wage) == int(other.wage)

    def __lt__(self, other):
        return int(self.wage) < int(other.wage)

    def __gt__(self, other):
        return int(self.wage) > int(other.wage)

    def __str__(self):
        return f""" Название вакансии: {self.name_vacancies},
    ссылка на вакансию: {self.url_vacancies},
    заработная плата: {self.wage},
    описание: {self.description}"""


class HHVacancies(Vacancy):
    def __str__(self):
        return f""" Название вакансии: {self.name_vacancies},
       ссылка на вакансию: {self.url_vacancies},
       заработная плата: {self.wage},
       описание: {self.description}"""


class SJVacancies(Vacancy):
    def __str__(self):
        return f""" Название вакансии: {self.name_vacancies},
       ссылка на вакансию: {self.url_vacancies},
       заработная плата: {self.wage},
       описание: {self.description}"""
