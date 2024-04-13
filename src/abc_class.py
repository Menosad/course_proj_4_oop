from abc import ABC, abstractmethod


class ABCParser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def get_vacancies(self):
        pass
