import os
import json
from src.class_vacancy import Vacancy
from colorama import init, Fore, Style


class Management:
    """Класс управляющий выводом вакансий на экран -> возвращает список
    всегда показывает сколько всего подобрано вакансий и какая по счету высвечена
    должен уметь листать вакансии по одной, нажатием на стрелочки, листаются по кругу, вперед и назад
    должен уметь добавлять (нажатием на пробел) в множество избранных вакансий из отфильтрованных
    должен уметь загружать список избранных вакансий, удалять оттуда"""

    def __init__(self):
        self.folder = os.path.abspath('')
        self.data_file_path = os.path.join(self.folder, 'data', 'favorites_vacancies.json')
        self.favorites_vacancies = []
        self.init_favorites_list()

    def __str__(self):
        return Fore.LIGHTYELLOW_EX + f"В избранном {len(self)} вакансий" + Style.RESET_ALL

    def __len__(self):
        return len(self.favorites_vacancies)

    def scroll_filtered_list(self, array):
        """Метод должен уметь листать вакансии по одной, нажатием на стрелочки, листаются по кругу, вперед и назад"""
        user_input = ''
        if len(array) == 0:
            print(Fore.LIGHTRED_EX + f"В избранном нет вакансий" + Style.RESET_ALL)
            return array
        while user_input != 'stop':
            for num, element in enumerate(array):
                print(Fore.LIGHTYELLOW_EX + f"{num + 1} из {len(array)} вакансий" + Style.RESET_ALL)
                print(element)
                user_input = input(Fore.LIGHTGREEN_EX + f"'Enter'" + Style.RESET_ALL + f"- листать дальше\t\t"
                                   + Fore.LIGHTGREEN_EX + f"введите 'add'" + Style.RESET_ALL + f" - что-бы добавить в избранное\t\t"
                                   + Fore.LIGHTGREEN_EX + f"'stop'" + Style.RESET_ALL + f" - завершить работу\n").strip().lower()
                if user_input == '':
                    continue
                elif user_input == 'add':
                    self.favorites_vacancies.append(element)
                elif user_input == 'stop':
                    self.uploading_favorites()
                    break

    def uploading_favorites(self):
        """Метод создающий файл с отфильтрованными вакансиями
        создает список словарей с доступом по ключу id, НЕ ФАЙЛ! ПЕРЕДЕЛАЙ!"""
        new_list = []
        with open(self.data_file_path, 'w') as file:
            for item in self.favorites_vacancies:
                new_list.append(item.__dict__)
            upload_json = json.dumps(new_list, ensure_ascii=False, indent=4)
            file.write(upload_json)

    def init_favorites_list(self):
        """Метод инициализирующий список избранных вакансий"""
        favorites_list = []
        if os.path.exists(self.data_file_path):
            with open(self.data_file_path, 'r') as file:
                try:
                    array = json.load(file)
                    for item in array:
                        id = item['id']
                        name = item['name']
                        address_city = item['address_city']
                        employer_name = item['employer_name']
                        salary = item['salary']
                        requirement = item['requirement']
                        responsibility = item['responsibility']
                        experience = item['experience']
                        url = item['url']
                        vac = Vacancy(id, name, address_city, salary, employer_name, requirement,
                                      responsibility, experience, url)
                        vac.salary_text = vac.validate()
                        favorites_list.append(vac)
                    self.favorites_vacancies = favorites_list
                except ValueError:
                    print(Fore.LIGHTRED_EX + f"Вакансий не подобрано, начните поиск заново!" + Style.RESET_ALL)
                    return False
            return True
        else:
            return False

    def scroll_favorites(self):
        """Метод просматривает список избранных вакансий"""
        user_input = ''
        while user_input != False:
            for num, item in enumerate(self.favorites_vacancies):
                print(self)
                print(item)
                print(Fore.LIGHTGREEN_EX + f"'Enter'" + Style.RESET_ALL + f" - следующая вакансия\tнапишите " + Fore.LIGHTGREEN_EX + f"del" + Style.RESET_ALL + f" - чтобы удалить текущую вакансию из избранного\n"
                      + Fore.LIGHTGREEN_EX + f"'new'" + Style.RESET_ALL + f" - новый поиск вакансий" + Style.RESET_ALL)
                user_input = input()
                if user_input == 'del':
                    del self.favorites_vacancies[num]
                elif user_input == 'new':
                    user_input = False
                    break
        self.uploading_favorites()

    def obtaining_vacancy_objects(self, array):
        """Функция для составления списка объектов Vacancy"""
        list_objects = []
        for item in array:
            id = item['id']
            name = item['name']
            address_city = item['area']['name'].lower()
            salary = item['salary']
            employer_name = item['employer']['name']
            requirement = item['snippet']['requirement']
            responsibility = item['snippet']['responsibility']
            experience = item['experience']['name']
            url = item['apply_alternate_url']
            vacancy = Vacancy(id, name, address_city, salary, employer_name, requirement,
                              responsibility, experience, url)
            vacancy.salary_text = vacancy.validate()
            list_objects.append(vacancy)
        return list_objects
