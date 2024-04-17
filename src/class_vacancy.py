class Vacancy:
    __slots__ = ['id_num', 'name', 'address_city', 'salary', 'employer_name',
                 'requirement', 'responsibility', 'experience', 'url', 'salary_text']
    id_num: int
    name: str
    address_city: str
    employer_name: str
    requirement: str
    responsibility: str
    experience: str
    url: str

    def __init__(self, id_num, name, address_city, salary, employer_name, requirement,
                 responsibility, experience, url):
        self.id_num = id_num
        self.name = name
        self.address_city = address_city
        self.employer_name = employer_name
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.experience = experience
        self.url = url
        self.salary_text = self.validate()

    def __str__(self):
        return (f"Вакансия: {self.name} от компании {self.employer_name} в городе {self.address_city.capitalize()}.\n"
                f"{self.salary_text}. Опыт работы: {self.experience} \n"
                f"Необходимые навыки: {self.requirement}\n"
                f"Вам предстоит {self.responsibility}\n"
                f"--------------------------------")

    def validate(self):
        if self.salary is None:
            self.salary = [0]
            return 'Зарплата не указана'
        else:
            salary_from = self.salary['from']
            salary_to = self.salary['to']
            shaft = self.salary['currency']
            self.salary = [salary_from, salary_to, shaft]
            if salary_from is None:
                self.salary = [salary_to, shaft]
                return f"Зарплата от: {salary_to} {shaft}"
            elif salary_to is None:
                self.salary = [salary_from, shaft]
                return f"Зарплата от: {salary_from} {shaft}"
            else:
                return f"Зарплата от: {salary_from} до {salary_to} {shaft}"


