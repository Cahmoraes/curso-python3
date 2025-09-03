from typing import Literal
from abc import ABC, abstractmethod

status_types = Literal["admin", "member", "editor"]


class User(ABC):
    @abstractmethod
    def __init__(self, name: str, id: int, status: status_types):
        self.__name = name
        self.__id = id
        self.__status = status

    def __str__(self):
        return f"Meu nome é {self.__name}"


class Member(User):
    def __init__(self, name: str, id: int, status: status_types, salary: float):
        super().__init__(name, id, status)
        self.__salary = salary

    @property
    def salary(self):
        return f"{self.__salary:.2f}"

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary


user = Member(name="Caique", id=1, status="member", salary=2)


print(user)
print(user.salary)
user.salary = 5.2
print(user.salary)
