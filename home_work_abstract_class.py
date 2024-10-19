### home_work_abstract_class.py
""" Иерархия сотрудников и задачи проекта.

Требования: Создайте систему классов для управления сотрудниками, задачами и проектами в компании.
1. Создайте абстрактный класс Employee с атрибутами:
◦ Имя, Роль (менеджер, разработчик и т.д.), Метод work(), который будет реализован в подклассах для выполнения конкретных обязанностей.
2. Создайте классы для разных типов сотрудников:
◦ Developer (разработчик): реализуйте метод work() для выполнения программирования.
◦ Tester: реализуйте метод work() для тестирования кода.
◦ Manager: метод work() будет управлять командой.
2. Создайте класс Task, который содержит задачу и ссылку на сотрудника, который её выполняет.
4. Создайте класс Project, который содержит несколько задач и сотрудников.
Перегрузите операторы сравнения для сотрудников (==, >, <), чтобы можно было сравнивать сотрудников по количеству выполненных задач.
Используйте множественное наследование, например, для создания класса LeadDeveloper, который является одновременно разработчиком и менеджером, чтобы он мог выполнять обе роли (программировать и управлять командой)."""

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, role=None, count_tasks=0):
        self.name = name
        self.role = role
        self.count_tasks = count_tasks

    @abstractmethod
    def work(self):
        pass

    def __eq__(self, other):
        return self.count_tasks == other.count_tasks
    def __gt__(self, other):
        return self.count_tasks > other.count_tasks
    def __lt__(self, other):
        return self.count_tasks < other.count_tasks

class Developer(Employee):
    def __init__(self, name, role='developer', task=None):
        super().__init__(name, role)
        self.task_dev = task
        self.task_dev = 'программирует'
        self.task = self.task_dev
        self.count_tasks = []

    def work(self):
        print(f'Сотрудник {self.name} - {self.role}. Функции: {self.task}')

    def add_tasks(self, *args):
        if args is not None and args not in self.count_tasks:
            self.count_tasks += args
            return len(self.count_tasks)

class Tester(Employee):
    def __init__(self, name, role='tester', task=None):
        super().__init__(name, role)
        self.task_test = task
        self.task_test = 'тестирует код'
        self.task = self.task_test
        self.count_tasks = []

    def work(self):
        print(f'Сотрудник {self.name} - {self.role}. Функции: {self.task}')

    def add_tasks(self, *args):
        if args is not None and args not in self.count_tasks:
            self.count_tasks += args
        return len(self.count_tasks)

class Manager(Employee):
    def __init__(self, name, role='manager', task=None):
        super().__init__(name, role)
        self.task_man = task
        self.task_man = 'управляет командой'
        self.task = self.task_man
        self.count_tasks = []

    def work(self):
        print(f'Сотрудник {self.name} - {self.role}. Функции: {self.task}')
      
    def add_tasks(self, *args):
        if args is not None and args not in self.count_tasks:
            self.count_tasks += args
        return len(self.count_tasks)

class LeadDeveloper(Developer, Manager):
    def __init__(self, name, role='leadDeveloper', task=None):
        Developer.__init__(self, name, role, task)
        Manager.__init__(self, name, role, task)
        self.task = task
        self.task = self.task_man + ', ' + self.task_dev
        self.count_tasks = []

    def add_tasks(self, *args):
        if args is not None and args not in self.count_tasks:
            self.count_tasks += args
        return len(self.count_tasks)

class Project():
    def __init__(self, name):
        self.name = name
        self.tasks_in_project = []
        self.employees = []
        self.count_tasks = 0
        self.count_employees = 0

    def add_task_in_project(self, task=None):
        if task is not None and task not in self.tasks_in_project:
            self.tasks_in_project.append(task)
            self.count_tasks += 1
        return self.tasks_in_project

    def add_employee(self, employee=None):
        if employee is not None and employee not in self.employees:
            self.employees.append(employee)
            self.count_employees += 1
        return self.employees

    def __str__(self):
        return f'Project is [{self.name}] - {self.count_tasks} tasks: {self.tasks_in_project}\n\t\t\t\t\t\t  {self.count_employees} employees: {self.employees}'

class Task():
    def __init__(self, task):
        self.task = task
        self.employees = []
        self.tasks = []

    def add_task(self, task, employee=None):
        if task not in self.tasks:
            self.tasks.append(task)
        return self.tasks

    def add_employee(self, employee=None):     № содержит ссылку на сотрудника, который её выполняет - НЕ МОГУ СДЕЛАТЬ ССЫЛКУ НА СОТРУДНИКА((
        if employee is not None and employee not in self.employees:
            self.employees.append(employee)

    def __str__(self):
        return f'Task is [{self.task}]. Employee: {self.employees}'

employee1 = 'John'
employee2 = 'Kate'
employee3 = 'Ivan'
employee4 = 'Pol'

task_1 = 'закупка и поставка фейерверков'
task_2 = 'закупка и поставка напитков'
task_3 = 'поставка шариков'
task_4 = 'создание игры'

tester1 = Tester(employee1)
tester1.work()

developer1 = Developer(employee2)
developer1.work()

manager1 = Manager(employee3)
manager1.work()

leadDeveloper1 = LeadDeveloper(employee4)
leadDeveloper1.work()
print()

print(tester1.add_tasks(task_1, task_4, task_3))
print(developer1.add_tasks(task_2, task_3))

print(Employee.__gt__(developer1, tester1))
print(Employee.__lt__(developer1, tester1))
print(Employee.__eq__(tester1, developer1)) 

print(manager1.add_tasks(task_1, task_2))
print(manager1.add_tasks(task_3))

print(Employee.__eq__(manager1,tester1))   # не работает сравнение на ==
print(Employee.__gt__(manager1, developer1))


task1 = Task(task_1)
task1.add_task(task_1, None)
task1.add_employee(employee1)
task1.add_employee(employee2)
print(task1)

task2 = Task(task_2)
task2.add_task(task_2, None)
task2.add_employee(employee3)
task2.add_employee(employee4)
print(task2)
print()

project1 = Project('Корпоратив')
project1.add_task_in_project(task_1)
project1.add_task_in_project(task_2)
project1.add_employee(employee1)
project1.add_employee(employee2)
project1.add_employee(employee3)
project1.add_employee(employee4)
print(project1)
