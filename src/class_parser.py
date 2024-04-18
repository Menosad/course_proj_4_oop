from src.abc_class_parser import ABCParser
import requests
import os
import json


class ParserHH(ABCParser):
    folder = os.path.abspath('')
    data_path = os.path.join(folder, 'data', 'data_json_hh.json')

    def __init__(self):
        self.hh_url = 'https://api.hh.ru/vacancies'
        self.head = {'Agent-User': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 5}
        self.vacancies_list = []

    def get_vacancies(self, text=''):
        self.params['text'] = text
        ParserHH.refresh_data()
        while self.params['page'] != 4:
            response = requests.get(self.hh_url, headers=self.head, params=self.params)
            json_response = response.json()['items']
            self.vacancies_list.extend(json_response)
            self.params['page'] += 1
        extended_list = json.dumps(self.vacancies_list, ensure_ascii=False, indent=4)
        with open(ParserHH.data_path, 'w', encoding="utf-8") as f:
            f.write(extended_list)

        return self.vacancies_list

    @staticmethod
    def refresh_data():
        with open(ParserHH.data_path, 'w') as file:
            file.write('')
