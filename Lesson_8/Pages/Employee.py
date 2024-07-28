import requests 
import json
from Lesson_8.constants import X_client_URL

path = '/employee'

class Company:
    def __init__(self, url = X_client_URL):
        self.url = url
    
    #Создание компании
    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/company', headers=headers, params=body)
        return response.json()
    
    #Последнее создание компании
    def last_company_id(self):
        active_params = {'active': 'true' }
        response = requests.get(
            self.url + '/company', params=active_params)
        return response.json()[-1]['id']
    

class Employer:
    def __init__(self, url= X_client_URL):
        self.url = url

    #Список сотрудников компании
    def get_list(self, company_id: int):
        co = {'company': company_id}
        response = requests.get(self.url + '/employee', params=co)
        return response.json()

    #Добавление сотрудника
    def add_new(self, token: str, body : json):
        hdrs = {'x-client-token': token}
        resp = requests.post(self.url + '/employee', headers=hdrs, json=body)
        return resp.json()

    #Получить сотрудника по id
    def get_info(self, employee_id: int):
        resp = requests.get(self.url + path + str(employee_id))
        return resp.json()

    #Изменение инф-ии о сотруднике
    def change_info(self, token :str, employee_id: int, body: json):
        hdrs = {'x-client-token': token}
        resp = requests.patch(self.url + path + str(employee_id), headers=hdrs, json=body)
        return resp    