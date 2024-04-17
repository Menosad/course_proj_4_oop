class Vacancy:
    __slots__ = ['id_num', 'name', 'address_city', 'salary', 'salary', 'employer_name',
                 'requirement', 'responsibility', 'experience', 'url']
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
        Vacancy.validate(self)

    def __str__(self):
        return (f"Вакансия: {self.name} от компании {self.employer_name} в городе {self.v}.\n"
                f"{self.salary}. Опыт работы: {self.experience} \n"
                f"Необходимые навыки: {self.requirement}\n"
                f"Вам предстоит {self.responsibility}\n"
                f"--------------------------------")

    def validate(self):
        if not self.salary:
            salary_text = 'Зарплата не указана'
        else:
            if not self.salary['from']:
                salary_text = f"Зарплата: до {self.salary['to']}"
            elif not self.salary['to']:
                salary_text = f"Зарплата: от {self.salary['from']}"
            else:
                salary_text = f"Зарплата: от {self.salary['from']} до {self.salary['to']}"
        self.salary = salary_text
        return self.salary
