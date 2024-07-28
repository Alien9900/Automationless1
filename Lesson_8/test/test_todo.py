import pytest
from Lesson_8.Pages.ToDoMain import Task

zadacha = Task()

def test_todo():
    ##Получение списка задач
    list = zadacha.get_list()
    assert list.status_code == 200
    
    ##Создание новой задачи
    params = {"title": 'Задача', "completed": 'false'}
    task = zadacha.create(params)
    assert task is not None

    ##Переименование задачи
    params = {"title": 'Задача срочная'}
    rename_task = zadacha.rename(task,params)
    ##Проверяем что задача изменена
    assert rename_task.json()['title'] == 'Задача срочная'

    ##Получение информации по созданной задаче
    info = zadacha.info(task)
    #Проверяем соответствие созданной задачи
    assert info.json()['title'] == 'Задача срочная'
    assert info.json()['id'] == task
    
    ##Отметка задачи - выполнена
    params = {"completed": 'true'}
    sts_true = zadacha.change_status(task, params)
    assert sts_true == True

    ##Снятие отметки задачи - выполнена
    params = {"completed": 'false'}
    sts_false = zadacha.change_status(task,params)
    assert sts_false == False

    ##Удаление задачи 
    dlte = zadacha.delete(task)
    assert dlte == 204