from pathlib import Path
HH_URL = 'https://api.hh.ru/vacancies'
SP_URL = 'https://api.superjob.ru/2.0/vacancies/'
ROOT_PATH = Path(__file__).resolve().parent
SAVE_VACANCY =ROOT_PATH.joinpath("save_vacancy.json")

