from abc import ABC, abstractmethod


class ABCParser(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass
