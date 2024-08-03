import pytest
import requests 
from Lesson_8.Pages.Employee import Employer
from Lesson_8.Pages.Company import Company

employer = Employer()
company = Company()


def test_auth(get_token):
    token = get_token
    #Проверка,что токен не пустой
    assert token is not None
    #Токен обозначается в строковом формате
    assert isinstance(token, str)


def test_getcompany_id():
    name = 'HW8'
    descr = 'Skypro'
    result = company.create_company(name, descr)
    comp_id = result["id"]
    
    new_comp = company.get_company(comp_id)
    assert new_comp["id"]


def test_add_employer(get_token):
    token = str(get_token)
    company_id = company.last_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastname': 'Petrov',
        'middlename': 'string',
        'companyId': company_id,
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
    with pytest.raises(TypeError, match='get_list\\(\\) missing 1 required positional argument: \'company_id\''):
        employer.get_list()

# Проверяем, что обязательное поле 'ID компании' в запросе на получение информации о сотрудниках не валидно
def test_get_list_employers_inval_compId():
    with pytest.raises(TypeError, match='get_list\\(\\) missing 1 required positional argument: \'company_id\''):
        employer.get_list()

# Проверяем обязательное поле 'ID сотрудника' в запросе на получение информации о сотруднике без ID
def test_get_info_missing_employerId():
    with pytest.raises(TypeError, match='get_info\\(\\) missing 1 required positional argument: \'employee_id\''):
        employer.get_info()


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

# Проверяем обязательные поля 'employee_id', 'token' и 'body' в запросе на изменение информации о сотруднике
def test_employers_missing_id_and_token():
    with pytest.raises(TypeError, match="change_info\(\) missing 3 required positional arguments: 'employee_id', 'token', and 'body'"):
        employer.change_info()