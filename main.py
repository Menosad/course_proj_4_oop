import json
from src.class_parser import ParserHH
from src.class_vacancy import Vacancy
from src.class_job_compression import JobCompression
import os


def get_vacancies_list():
    folder = os.path.abspath('data/data_json_hh.json')
    list_vacancies = []

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


if __name__ == '__main__':
    hh_parser = ParserHH()
    word = input('Название вакансии: ')
    hh_parser.get_vacancies(word)
    vacancies_list = get_vacancies_list()
    job_comp = JobCompression(vacancies_list)
    favorites_list = job_comp.filter()
    print('--------------------------------')
    for item in favorites_list:
        print(item)


