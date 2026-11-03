
from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, person_id):
        self._name = name
        self._id = person_id

    @abstractmethod
    def role(self):
        pass
