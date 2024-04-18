import os
import json

class JobCompression:
    __slots__ = ['array', 'favorite_list']
    folder_path = os.path.abspath('')
    data_file_path = os.path.join(folder_path, 'data', 'favorites_data.json')

    array: list
    favorite_list: list

    def __init__(self, array):
        self.array = array
        self.favorite_list = []

    def filter(self):
        """Метод фильтрующий список вакансий"""
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
        city = input('"Enter" - выбрать вакансии во всех городах\n'
                     'или укажите интересущий вас город: ').lower()
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
            print(f"{city} нет в списке, возможно вы имели в виду:\n"
                  f"{', '.join(list_of_matches)}")
            city = input(f"Нажмите 'Enter' - Все доступные города.\n"
                         f"или укажите город из списка: ")
            if city in list_of_matches:
                return city
            else:
                return ''

    def uploading_favorites(self):
        """Метод для добавления вакансий в избранное"""
        with open(self.data_file_path, 'w') as file:
            upload_json = json.dumps(str(self.favorite_list), ensure_ascii=False, indent=4)
            file.write(upload_json)
