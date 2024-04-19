from src.abc_class_parser import ABCParser
import requests
import os
import json


class ParserHH(ABCParser):
    __slots__ = ['hh_url', 'head', 'params', 'vacancies_list']

    """Класс для поиска вакансий на hh.ru
    умеет искать по запросу text
    должен уметь обноавлять избранные вакансии"""

    def __init__(self):
        self.hh_url = 'https://api.hh.ru/vacancies'
        self.head = {'Agent-User': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 5}
        self.vacancies_list = []
        self.folder = os.path.abspath('')
        self.data_path = ''

    def get_vacancies(self, text=''):
        self.params['text'] = text
        self.refresh_data()
        while self.params['page'] != 4:
            response = requests.get(self.hh_url, headers=self.head, params=self.params)
            json_response = response.json()['items']
            self.vacancies_list.extend(json_response)
            self.params['page'] += 1
        extended_list = json.dumps(self.vacancies_list, ensure_ascii=False, indent=4)
        with open(self.data_path, 'w') as f:
            f.write(extended_list)
        return self.vacancies_list

    def refresh_data(self):
        self.data_path = os.path.join(self.folder, 'data', 'data_json_hh.json')
        with open(self.data_path, 'w') as file:
            file.write('')
