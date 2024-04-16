import json
from src.class_parser import ParserHH
from src.class_vacancy import Vacancy
import os


def get_vacancies_list():
    folder = os.path.abspath('data/data_json_hh.json')
    list_vacancies = []

    with open(folder) as file:
        data_dict = json.load(file)
    for item in data_dict:
        id_num = item['id']
        name = item['name']
        address_city = item['area']['name']
        salary = item['salary']
        employer_name = item['employer']['name']
        requirement = item['snippet']['requirement']
        responsibility = item['snippet']['responsibility']
        vacancy = Vacancy(id_num, name, address_city, salary, employer_name, requirement,
                          responsibility)
        list_vacancies.append(vacancy)

    return list_vacancies


vacancies_list = get_vacancies_list()

for item in vacancies_list:
    # id_num = item['id']
    # name = item['name']
    # address_city = item['area']['name']
    # salary = item['salary']
    # employer_name = item['employer']['name']
    # requirement = item['snippet']['requirement']
    # responsibility = item['snippet']['responsibility']
    print(f"Вакансия: {item.name}\n"
          f"от компании {item.employer_name} в городе {item.address_city}")
    if not item.salary:
        print('Зарплата не указана')
    else:
        print(f"Зарплата: от {item.salary['from']} до {item.salary['to']}")

