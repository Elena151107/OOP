## DECORATOR
## home_work_decorator.py

""" Задача 1: Декоратор для проверки прав доступа.
Создайте декоратор, который проверяет, есть ли у пользователя необходимые права доступа для выполнения
функции. Если прав недостаточно, функция должна возвращать сообщение об ошибке."""

def requires_permission(permission):
    def decor(func):
        def wrapper(*args):
            if permission not in args:
                print('Доступ закрыт')
                return func(*args)
            return f'Вы администратор, доступ разрешен'
        return wrapper
    return decor

@requires_permission('admin')
def delete_user(user_id):
    return f'User [{user_id}] deleted'

print(delete_user('admin'))



""" Задача 2: Декоратор для преобразования результата.
Создайте декоратор, который преобразует результат функции в строку. Если результат уже строка, он должен возвращаться без изменений."""


def to_string(func):
    def wrapper():
        result = func()
        if type(result) == str:
            print(type(result))
            return func()
        else:
            result = str(result)
            print(type(result))
            return func()
    return wrapper

@to_string
def get_number():
    return 42

@to_string
def get_text():
    return "Hello, World!"

print(get_number())
print(get_text())
