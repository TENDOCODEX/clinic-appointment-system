
from abc import ABC, abstractmethod


class Person(ABC):
    _constructed_count = 0

    def __init__(self, name, person_id):
        # Validate name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")

        # Validate ID
        if isinstance(person_id, bool) or not isinstance(person_id, int) or person_id <= 0:
            raise ValueError("ID must be a positive integer")

        Person._constructed_count += 1

        # Private attributes
        self.__name = name.strip()
        self.__id = person_id

    @property
    def name(self):
        return self.__name

    @property
    def person_id(self):
        return self.__id

    @abstractmethod
    def role(self):
        pass
