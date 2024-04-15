class Vacancy:
    __slots__ = ['id_num', 'name', 'address_city', 'salary', 'salary', 'employer_name',
                 'requirement', 'responsibility']
    id_num: int
    name: str
    address_city: str
    salary: dict
    employer_name: str
    requirement: str
    responsibility: str

    def __init__(self, id_num, name, address_city, salary, employer_name, requirement,
                 responsibility):
        self.id_num = id_num
        self.name = name
        self.address_city = address_city
        self.employer_name = employer_name
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        Vacancy.validate()

    def job_comparisons(self):
        pass

    @staticmethod
    def validate():
        params = Vacancy.__dict__
        for key in params.keys():
            if not params[key]:
                Vacancy.key = 'Не указано'


    pass
