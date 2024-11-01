#### metaclass_home_work.py

""" Создайте метакласс InfoMeta.

- При создании класса с этим метаклассом он должен автоматически добавлять метод info, который возвращает строку вида "Класс <ИмяКласса>: атрибуты <список_атрибутов>"
- Создайте несколько классов, используя InfoMeta как метакласс, и добавьте в них разные атрибуты.
- Создайте объекты этих классов и вызовите у них метод info, чтобы убедиться, что он корректно отображает информацию о классе.
Пример:
class MyClass(metaclass=InfoMeta): 
x = 10 
y = 20 
oJj = MyClass() 
print(oJj.info()) 
# Ожидаемый вывод: "Класс MyClass: атрибуты ['x', 'y']"
Подсказка: Для реализации метода info в метаклассе используйте cls.__name__ и cls.__dict__ для получения имени класса и его атрибутов."""

class InfoMeta(type):

    def __new__(cls, name, bases, dct):
        def info(self):
            list_attr = {}
            for name_attr, value in self.__dict__.items():
                if name_attr.startswith('__'):
                    continue
                if hasattr(value, 'info') and callable(value.info):
                    list_attr[name_attr] = value.info()
                else:
                    list_attr[name_attr] = value
            list_attr = [i for i, j in list_attr.items()]
            return f'Класс {name}: атрибуты {list_attr}'
        dct['info'] = info
        return super().__new__(cls, name, bases, dct)

class MyClass_1(metaclass=InfoMeta):
    def __init__(self):
        self.x = 10
        self.y = 20
obj1 = MyClass_1()
print(obj1.info())

class MyClass_2(metaclass=InfoMeta):
    def __init__(self):
        self.z = 10
        self.w = 20
        self.q = 30
obj2 = MyClass_2()
print(obj2.info())

class MyClass_3(metaclass=InfoMeta):
    def __init__(self):
        self.t = 10
        self.p = 20
        self.m = 30
        self.name = 'Kate'
obj3 = MyClass_3()
print(obj3.info())
