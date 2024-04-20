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
        self.params = {'text': '', 'page': 0, 'per_page': 10}
        self.vacancies_list = []

    def get_vacancies(self, text=''):
        self.params['text'] = text
        while self.params['page'] != 10:
            response = requests.get(self.hh_url, headers=self.head, params=self.params)
            json_response = response.json()['items']
            self.vacancies_list.extend(json_response)
            self.params['page'] += 1
        return self.vacancies_list

