import pytest
from Lesson_8.Pages.ToDoMain import Task

new_task = Task()

def test_todo():
    ##Получение списка задач
    list = new_task.get_list()
    assert list.status_code == 200
    
    ##Создание новой задачи
    params = {"title": 'Задача', "completed": 'false'}
    task = new_task.create(params)
    assert task is not None

    ##Переименование задачи
    params = {"title": 'Задача срочная'}
    rename_task = new_task.rename(task,params)
    ##Проверяем что задача изменена
    assert rename_task.json()['title'] == 'Задача срочная'

    ##Получение информации по созданной задаче
    info = new_task.info(task)
    #Проверяем соответствие созданной задачи
    assert info.json()['title'] == 'Задача срочная'
    assert info.json()['id'] == task
    
    ##Отметка задачи - выполнена
    params = {"completed": 'true'}
    sts_true = new_task.change_status(task, params)
    assert sts_true == True

    ##Снятие отметки задачи - выполнена
    params = {"completed": 'false'}
    sts_false = new_task.change_status(task,params)
    assert sts_false == False

    ##Удаление задачи 
    dlte = new_task.delete(task)
    assert dlte == 204