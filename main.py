import json
from src.class_parser import ParserHH
from src.class_vacancy import Vacancy
from src.class_job_compression import JobCompression
import os


def obtaining_vacancy_objects():
    """Функция для составления списка объектов Vacancy"""
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
    # мэйн должен работать через цикл while пока не нажать Esc
    """мэйн общается с пользователем: 
    Привет, давай подберем тебе работу!
    у тебя в избранном:
    (если есть) по запросу {название запроса} {количество избранных вакансий } вакансий
    желаете просмотреть вакансии в избранном?
    в {имя запроса} {количество избранных вакансий} 
    ОБНОВИТЬ - 'Space'
    ВЫВЕСТИ - 'Enter'
    я буду работать: 
    с зарплатой от:
    ищу в городе: 
    вы добавили в избранное {количество избранных вакансий} вакансий по запросу {название запроса}"""
    text = ''
    while text != 'stop':
        hh_parser = ParserHH()
        print('Привет, давай подберем тебе работу!')
        text = input('вакансия: ')
        uploaded_vacancies_list = hh_parser.get_vacancies(text)
        vacancies_list = obtaining_vacancy_objects()
        job_compres = JobCompression(vacancies_list)
        job_compres.filter()
        job_compres.uploading_favorites(text)
        break
        # у тебя в избранном:

        # text = input('Укажите искомую вакансию: ')
        # vacancies_list = hh_parser.get_vacancies(text)
        # vacancies_object_list = obtaining_vacancy_objects()
        # job_compression = JobCompression(vacancies_object_list)
        # favorites_list = job_compression.filter()
        #
        # for obj in favorites_list:
        #     print(obj)
