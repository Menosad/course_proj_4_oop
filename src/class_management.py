import os
import json
from src.class_vacancy import Vacancy


class Management:

    def __init__(self):
        list_vacancies = []
        folder = os.path.abspath('data/data_json_hh.json')

    def get_vacancies_list(self):

        with open(folder, encoding='utf-8') as file:
            data_dict = json.load(file)
        for item in data_dict:
            id_num = item['id']
            name = item['name']
            address_city = item['area']['name'].lower()
            salary = item['salary']
            employer_name = item['employer']['name']
            requirement = item['snippet']['requirement']
            responsibility = item['snippet']['responsibility']
            experience = item['experience']['name']
            url = item['apply_alternate_url']
            vacancy = Vacancy(id_num, name, address_city, salary, employer_name, requirement,
                              responsibility, experience, url)
            list_vacancies.append(vacancy)

        return list_vacancies

