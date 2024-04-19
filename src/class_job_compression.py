import os
import json


class JobCompression:
    __slots__ = ['array', 'favorite_list', 'data_file_path']
    folder_path = os.path.abspath('')

    array: list
    favorite_list: list

    def __init__(self, array):
        self.array = array
        self.favorite_list = []
        self.data_file_path = os.path.join(JobCompression.folder_path)

    def filter(self):
        """Метод фильтрующий список вакансий, возвращает список объектов Vacancy"""
        salary_from = ''
        while not isinstance(salary_from, int):
            try:
                salary_from = int(input('Зарплата от: '))
            except:
                print('Напишите 0 или искомую зарплату')
        city = self.city_filter()
        for item in self.array:
            if city == item.address_city and item.salary[0] >= int(salary_from):
                self.favorite_list.append(item)
            else:
                if item.salary[0] >= int(salary_from):
                    self.favorite_list.append(item)
        return self.favorite_list

    def city_filter(self):
        """Метод для выбора фильтра по городу"""
        cities = set()  # список городов для корректировки ввода от пользователя
        list_of_matches = []
        for city in self.array:
            cities.add(city.address_city)
        city = input('Нажмите "Enter" - все доступные города.\n'
                     'Укажите город, где хотите работать: ').lower()
        if city in cities:
            return city
        elif city == '':
            return city
        else:
            for element in cities:
                count = 0
                for letter in city:
                    if letter in element:
                        count += 1
                if count > len(city) // 2:
                    list_of_matches.append(element.capitalize())
            print(f"{city.capitalize()} нет в списке, возможно вы имели в виду:\n"
                  f"{', '.join(list_of_matches)}")
            city = input(f"или укажите город из списка: ")
            if city in list_of_matches:
                return city
            else:
                return ''

    def uploading_favorites(self, vacancy_name):
        """Метод создающий файл с отфильтрованными вакансиями
        создает список, НЕ ФАЙЛ! ПЕРЕДЕЛАЙ!"""
        file_name = 'hh_parser_' + vacancy_name + '.json'
        self.data_file_path = os.path.join('data', file_name)
        with open(self.data_file_path, 'w') as file:
            upload_json = json.dumps(str(self.favorite_list), ensure_ascii=False, indent=4)
            file.write(upload_json)
