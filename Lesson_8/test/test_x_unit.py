import pytest
import requests 
from Lesson_8.Pages.Employee import Employer, Company

employer = Employer()
company = Company()


def test_auth(get_token):
    token = get_token
    #Проверка,что токен не пустой
    assert token is not None
    #Токен обозначается в строковом формате
    assert isinstance(token, str)

def test_getcompany_id():
    company_id = company.last_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()

def test_add_employer(get_token):
    token = str(get_token)
    comp_id = company.last_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastname': 'Petrov',
        'middlename': 'string',
        'companyId': comp_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-06-12T22:45:36.6222',
        'isActive': 'true'
    }
    new_employId = (employer.add_new(token, body_employer))['id']
    #Проверка что id сотрудника не пустой
    assert new_employId is not None
    #Проверка что id сотрудника состоит из цифр
    assert str(new_employId).isdigit()


    #Получение инфомации о новом сотруднике
    info = employer.get_info(new_employId)
    #Сравение id сотрудника из списка с id при создании сотрудника
    assert info.json()['id'] == new_employId
    #Проверка на ответ 200 
    assert info.status_code == 200


#Проверка создания клиента без токена

def test_add_employer_without_token():
    comp_id = company.last_company_id()
    token = ""
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastname': 'Petrov',
        'middlename': 'string',
        'companyId': comp_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-06-12T22:45:36.6222',
        'isActive': 'true'
    }
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Unauthorized'


#Проверка невозможность создания сотрудника без тела запроса

def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_company_id()
    body_employer = {}
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Internal server error'

def test_get_employer():
    com_id = company.last_company_id()
    #Получаем список сотрудников компании
    list_employers = employer.get_list(com_id)
    assert isinstance(list_employers, list)

##Проверяем, обязательно поле 'ID компании' в запросе на получение списка работников без ID компании


def test_get_list_miss_comId():
    try:
        employer.get_list()
    except TypeError as e:
        assert str(e) == 'Employer.get_list() missing I required positional argument: "company_id"'


##Проверяем, обязательное поле 'ID компании' в запросе на получение списка работников не валидное ID компании

def test_get_list_employers_inval_compId():
    try:
        employer.get_info()
    except TypeError as e:
        assert str(e) ==  'Employer.get_info() missing I required positional argument: "company_id"'

##Проверяем обязательное поле 'ID сотрудника' в запросе на получение инф-ии о сотруднике без ID

def test_get_info_missing_employerId():
    try:
        employer.get_info()
    except TypeError as e:
        assert str(e) ==  'Employer.get_info() missing I required positional argument: "employee_id"'

##Проверяем изменение информации о сотруднике 
def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastname': 'Petrov',
        'middlename': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-06-12T22:45:36.6222',
        'isActive': 'true'
    }
    just_employer = employer.add_new(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
        'lastName': "Lozhkin",
        'email': 'test2@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200


    ###Проверяем что ID сотрудника соответствует ID при создании сотрудника
    assert id == employer_changed.json()['id']
    ##Проверяем что почта изменилась
    assert (employer_changed.json()["email"]) == body_change_employer.get("email")


###Проверяем обязательное поле "ID сотрудника", "token", "body" в запросе на изменение инф-ии о сотруднике без этих данных


def test_employers_missing_id_and_token():
    try:
        employer.change_info()
    except TypeError as e:
        assert str(e) == "Employer.get_change() missing 3 required positional argument: 'employee_id','token', and 'body'"