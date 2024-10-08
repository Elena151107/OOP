## DECORATOR
## home_work_decorator.py

""" Задача 1: Декоратор для проверки прав доступа.
Создайте декоратор, который проверяет, есть ли у пользователя необходимые права доступа для выполнения
функции. Если прав недостаточно, функция должна возвращать сообщение об ошибке."""

def requires_permission(permission):
    def decor(func):
        def wrapper(user_id):
            if user_id == permission:
                print(f'[{user_id}] Вы администратор, доступ разрешен')
            else:
                print('Доступ закрыт')
                print(func(user_id))
        return wrapper
    return decor

@requires_permission('admin')
def delete_user(user_id):
    return f'User [{user_id}] deleted'

delete_user('admin')



