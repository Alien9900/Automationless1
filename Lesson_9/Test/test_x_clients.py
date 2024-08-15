import pytest
import json
from Lesson_9.Pages.Employee import Employer
from Lesson_9.Pages.Database import DataBase

api = Employer("https://x-clients-be.onrender.com")
db = DataBase("postgresql+psycopg2://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")


def test_get_list_employers():
    # Создание компании
    db.create_company("Vladislav_QA", "SkyPro")
    # Получение id последней созданной компании
    max_id = db.last_company_id()
    print(max_id)
    # Добавление сотрудника в компанию
    db.create_employer(max_id, "Vladislav", "Ivashin", 80029396386)
    # Получение списка сотрудников последней компании
    db_employer_list = db.get_list_employer(max_id)
    # API получение списка сотрудников последней созданной компании
    api_employer_list = api.get_list(max_id)
    # Сравнение списка сотрудников API и БД
    assert len(api_employer_list) == len(db_employer_list)
    # Удаляем сотрудника компании
    response = (api.get_list(max_id))[0]
    employer_id = response['id']
    db.delete_employer(employer_id)
    # Удаляем последнюю созданную компанию
    db.delete(max_id)

    

def test_add_new_employer():
    #создание и получение id последней созданной компании
    db.create_company('Vladislav adding new employer', 'employer')
    max_id = db.last_company_id()
    # создание сотрудника 
    db.create_employer(max_id, "Vladislav","Ivashin", 80029396386)
    response = (api.get_list(max_id))[0]
    employer_id = response['id']
    #Cравнение id компании 
    assert response['companyId'] == max_id
    #Сравнение имени сотрудника с заданной ранее
    assert response['firstName'] == "Vladislav"
    #Удостоверяемся что статус сотрудника == true
    assert response['isActive'] == True
    #Сравнение фамилии сотрудника заданной ранее
    assert response['lastName'] == "Ivashin"
    # Удаление сотрудника
    db.delete_employer(employer_id)
    # Удаление компании
    db.delete(max_id)


def test_assertion_data():
    db.create_company("Employer get id company", 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vladislav", "Ivashin", 80029396386)
    employer_id = db.get_employer_id(max_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Vladislav"
    assert get_api_info["lastName"] ==  "Ivashin"
    assert get_api_info["phone"] ==  "80029396386"
    db.delete_employer(employer_id)
    db.delete(max_id)

def test_update_user_info():
    db.create_company('New updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vladislav", "Ivashin", 80029396386 )
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("Alien", employer_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Alien"
    assert get_api_info["lastName"] ==  "Ivashin"
    assert get_api_info["isActive"] == True
    db.delete_employer(employer_id)
    db.delete(max_id)  