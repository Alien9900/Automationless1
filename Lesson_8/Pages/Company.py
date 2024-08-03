import requests 
import json
from Lesson_8.constants import X_client_URL



class Company:
    def __init__(self, url = X_client_URL):
        self.url = url
    
    def get_company(self,id):
        resp = requests.get(self.url + '/company/'+ str(id))
        return resp.json()
    
    def create_company(self, name , description =''):
        company = {
            "name": name,
            "description": description 
        }
        my_headers = {'x-clien-token': company}
        resp = requests.post(self.url+ '/company', json=company, headers=my_headers)
        return resp.json()['userToken'] 
    #Последнее создание компании
    def last_company_id(self):
        active_params = {'active': 'true' }
        response = requests.get(
            self.url + '/company', params=active_params)
        return response.json()[-1]['id']
    
