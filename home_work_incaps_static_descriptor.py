### home_work_incaps_static_descriptor.py

""" Задача: Управление курсами валют.
  Описание:
Создайте систему для управления курсами валют. Система должна позволять устанавливать курсы валют, проверять
корректность курса и конвертировать суммы между разными валютами. 
- Класс Currency будет хранить информацию о валюте и её курсе.
- Класс CurrencyConverter будет отвечать за конвертацию между валютами.
Инкапсуляция:
- Поле, которое хранит курс валюты, должно быть защищённым (private). Оно должно быть доступно только через специальные методы.
Статический метод:
- еализуйте статический метод, который проверяет корректность курса валюты Rнапример, 
курс должен быть положительным числом.
Дескриптор:
- Используйте дескриптор для валидации кода валюты. Код валюты должен состоять из трёх заглавных букв
(например, "USD", "EUR").
  Условия:
1. Создайте класс Currency, который будет хранить код валюты и её курс относительно доллара США.
2. Используйте инкапсуляцию для поля rate, которое будет хранить курс валюты. Доступ к этому полю должен осуществляться
   только через методы set_rate и get_rate.
3. Статический метод должен проверять, что курс валюты корректен (положительное число)
4. Используйте дескриптор для проверки кода валюты (он должен состоять из трёх заглавных букв)
5. Создайте класс CurrencyConverter, который будет принимать две валюты и сумму, и конвертировать сумму из одной валюты в другую."""

class Desc():
    def __get__(self, instance, owner):
        return instance.__dict__['code']

    def __set__(self, instance, value):
        if len(value) == 3 and value.isalpha() and value.isupper():
            instance.__dict__['code'] = value
        else:
            raise ValueError('Введен неверный код валюты')

class Currency():
    code = Desc()

    def __init__(self, code, rate=None):
        self.code = code
        self.__rate = Currency.is_positive_rate(rate)
        self.dict_codes = {
            self.code: self.__rate
    }

    @staticmethod
    def is_positive_rate(rate):
        if rate is None or not isinstance(rate, (int, float)) or rate < 0:
            raise ValueError('Курс валюты должен быть положительным')
        return rate

    def set_rate(self, rate):
        self.__rate = rate

    def get_rate(self):
        return self.__rate

    def add_codes(self):
        self.dict_codes.setdefault(self.code, self.get_rate())
        return self.dict_codes

class CurrencyConverter():
    def __init__(self):
        pass

    def converter_codes(self, from_code, to_code, amount=0):
        to_code = to_code.dict_codes
        from_code = from_code.dict_codes

        rate1 = 0
        code_to = ''
        for key, value in to_code.items():
            rate1 += value
            code_to += key
     
        rate2 = 0
        code_from = ''
        for key, value in from_code.items():
            rate2 += value
            code_from += key

        if amount > 0:
            summa = amount * (rate1 / rate2)
            return f'{amount} {code_from} = {summa: .3f} {code_to}'
        else:
            raise ValueError('Введите сумму больше 0')

codee = Currency('USA', 1)
code1 = Currency('RUB', 96.6657)
code2 = Currency('EUR', 0.9223 )
code3 = Currency('CNY', 7.1601 )
code4 = Currency('CHF', 0.8667 )

cur1 = CurrencyConverter()
print(cur1.converter_codes(code2, code1, 10))          ## 10 EUR =  1048.094 RUB
