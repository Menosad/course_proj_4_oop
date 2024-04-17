
class JobCompression:
    __slots__ = ['array', 'search_list']
    array: list
    search_list: list

    def __init__(self, array):
        self.array = array
        self.search_list = []


    def filter(self):
        """Метод фильтрующий список вакансий"""
        salary_from = int(input('Зарплата от: '))
        city = input('город, где хотите работать')
        for item in self.array:
            if item.address_city == city:
                if item.salary['from'] >= salary_from:
                    self.search_list.append(item)


    def add_to_favorites(self):
        pass

    pass
