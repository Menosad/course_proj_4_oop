class JobCompression:
    __slots__ = ['array', 'search_list']
    array: list
    search_list: list

    def __init__(self, array):
        self.array = array
        self.search_list = []

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
                self.search_list.append(item)
            else:
                if item.salary[0] >= int(salary_from):
                    self.search_list.append(item)
        return self.search_list

    def city_filter(self):
        """Метод для выбора фильтра по городу"""
        cities = set()  # список городов для корректировки ввода от пользователя
        list_of_matches = []
        for city in self.array:
            cities.add(city.address_city)
        city = input('Укажите город, где хотите работать: ').lower()
        if city in cities:
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

    def add_to_favorites(self):
        pass
