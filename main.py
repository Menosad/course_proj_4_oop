from src.class_parser import ParserHH
from src.class_job_compression import JobCompression
from src.class_management import Management


manage = Management()
hh_parser = ParserHH()


def parsing_hh():
    text = input('Вакансия: ')
    data_json_list = hh_parser.get_vacancies(text)
    vacancies_list = manage.obtaining_vacancy_objects(data_json_list)
    job_compres = JobCompression(vacancies_list)
    filtered_list = job_compres.filter()
    manage.scroll_filtered_list(filtered_list)
    return manage


if __name__ == '__main__':
    if len(manage) == 0:
        parsing_hh()
    elif manage.init_favorites_list():
        manage.scroll_favorites()
        parsing_hh()
    else:
        parsing_hh()
    print(manage)
