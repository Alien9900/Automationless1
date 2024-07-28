import requests
import json
from Lesson_8.constants import Todo_list_URL

class Task:
    def __init__(self, url = Todo_list_URL):
        self.url = url

    def get_list(self):
        resp = requests.get(self.url)
        return resp
    
    def create(self,params: json):
        resp = requests.post(self.url, json=params)
        return resp.json()['id']
    
    def rename(self, id: int, params: json):
        resp = requests.patch(self.url + str(id), json=params)
        return resp
    
    def info(self, id: int):
        resp = requests.patch(self.url + str(id))
        return resp
    
    def change_status(self, id: int, params: json):
        resp = requests.patch(self.url + str(id), json=params)
        status = resp.json()['completed']
        return status
    
    def delete(self, id: int):
        resp_status_code = (requests.delete(self.url + str(id))).status_code
        return resp_status_code