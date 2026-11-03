
from abc import abstractmethod
from src.person import Person


class Staff(Person):

    @abstractmethod
    def fee(self):
        pass
