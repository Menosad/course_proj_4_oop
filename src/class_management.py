import os


class Management:
    """Класс управляющий выводом вакансий на экран -> возвращает список
    всегда показывает сколько всего подобрано вакансий и какая по счету высвечена
    должен уметь листать вакансии по одной, нажатием на стрелочки, листаются по кругу, вперед и назад
    должен уметь добавлять (нажатием на пробел) в множество избранных вакансий из отфильтрованных
    должен уметь загружать список избранных вакансий, удалять оттуда"""
    
    def __init__(self, file_name):
        self.folder = os.path.abspath('')
        self.file_name = 'hh_' + file_name + '.json'
        self.data_file_path = os.path.join(self.folder, 'data', )

    def vacancy_rolling(self, array):
        """Метод должен уметь листать вакансии по одной, нажатием на стрелочки, листаются по кругу, вперед и назад"""
        for element in array:
            print(element)
        pass

    def add_to_favorite(self):
        """Метода должен уметь добавлять (нажатием на пробел) в множество избранных вакансий из отфильтрованных"""
        pass

    def uploading_favorites(self, vacancy_name):
        """Метод создающий файл с отфильтрованными вакансиями
        создает список словарей с доступом по ключу id, НЕ ФАЙЛ! ПЕРЕДЕЛАЙ!"""
        file_name = 'hh_parser_' + vacancy_name + '.json'
        self.data_file_path = os.path.join('data', file_name)
        with open(self.data_file_path, 'w') as file:
            upload_json = json.dumps(str(self.favorite_list), ensure_ascii=False, indent=4)
            file.write(upload_json)

    def delete(self):
        """Удаляет вакансии из избранного"""
        pass
