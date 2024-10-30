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
    def __init__(self, name, role=None, count_tasks=[]):
        self.name = name
        self.role = role
        self.count_tasks = count_tasks

    @abstractmethod
    def work(self):
        pass

    def add_tasks(self, *args):
        for arg in args:
            for elem in arg.tasks:
                self.count_tasks.append(elem)
            if isinstance(arg, Task):
                if self.name not in arg.employees:
                    arg.employees.append(self.name)
            print(arg)

    def __eq__(self, other):
        return len(self.count_tasks) == len(other.count_tasks)
    def __gt__(self, other):
        return len(self.count_tasks) > len(other.count_tasks)
    def __lt__(self, other):
        return len(self.count_tasks) < len(other.count_tasks)

class Developer(Employee):
    def __init__(self, name, role='developer', task=None):
        super().__init__(name, role)
        self.task_dev = task
        self.task_dev = 'программирует'
        self.task = self.task_dev
        self.count_tasks = []

    def work(self):
        print(f'Сотрудник {self.name} - {self.role}. Функции: {self.task}')

class Tester(Employee):
    def __init__(self, name, role='tester', task=None):
        super().__init__(name, role)
        self.task_test = task
        self.task_test = 'тестирует код'
        self.task = self.task_test
        self.count_tasks = []

    def work(self):
        print(f'Сотрудник {self.name} - {self.role}. Функции: {self.task}')

class Manager(Employee):
    def __init__(self, name, role='manager', task=None):
        super().__init__(name, role)
        self.task_man = task
        self.task_man = 'управляет командой'
        self.task = self.task_man
        self.count_tasks = []

    def work(self):
        print(f'Сотрудник {self.name} - {self.role}. Функции: {self.task}')

class LeadDeveloper(Developer, Manager):
    def __init__(self, name, role='leadDeveloper', task=None):
        Developer.__init__(self, name, role, task)
        Manager.__init__(self, name, role, task)
        self.task = task
        self.task = self.task_man + ', ' + self.task_dev
        self.count_tasks = []

class Task():
    def __init__(self, task):
        self.task = task
        self.tasks = self.add_task()
        self.employees = []

    def add_task(self):
        all_task = []
        if self.task not in all_task:
            all_task.append(self.task)
        return all_task

    def __str__(self):
        return f'Task is {self.tasks} - employee: {self.employees}'

class Project():
    def __init__(self, name):
        self.name = name
        self.tasks_in_project = []
        self.employees = []

    def add_task_in_project(self, *args):
        for arg in args:
            if isinstance(arg, Task):
                self.tasks_in_project.append(arg.tasks)
                self.employees.append(arg.employees)
        return self.tasks_in_project, self.employees

    def __str__(self):
        return (f'Проект: [{self.name}] - задачи проекта: {[i for elem in self.tasks_in_project for i in elem]}'
                f' - список сотрудников: {list(set([i for elem in self.employees for i in elem]))}')

tester1 = Tester('John')
tester1.work()
developer1 = Developer('Kate')
developer1.work()
manager1 = Manager('Ivan')
manager1.work()
leadDeveloper1 = LeadDeveloper('Pol')
leadDeveloper1.work()
print()

task1 = Task('закупка и поставка фейерверков')
task2 = Task('закупка и поставка напитков')
task3 = Task('поставка шариков')
task4 = Task('создание игры')

print(tester1.add_tasks(task1, task2))
print(developer1.add_tasks(task1, task3))
print(manager1.add_tasks(task3, task4))
print(leadDeveloper1.add_tasks(task1, task2, task3, task4))
print()

project1 = Project('КОРПОРАТИВ')
project1.add_task_in_project(task1, task2)
print(project1)
print()

print('******* СРАВНЕНИЕ КОЛИЧЕСТВА ЗАДАЧ *******:')
print()
print(tester1.count_tasks)
print(developer1.count_tasks)
print(Employee.__eq__(tester1, developer1))
print(Employee.__gt__(developer1, tester1))
print(Employee.__lt__(developer1, tester1))
print()

print('******* СРАВНЕНИЕ КОЛИЧЕСТВА ЗАДАЧ *******:')
print()
print(manager1.count_tasks)
print(leadDeveloper1.count_tasks)
print(Employee.__eq__(leadDeveloper1,manager1))
print(Employee.__gt__(manager1, leadDeveloper1))
print(Employee.__lt__(manager1, leadDeveloper1))
