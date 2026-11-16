
from abc import abstractmethod
from src.person import Person


class Staff(Person):

    @property
    def gap_hours(self):
        return 0

    @abstractmethod
    def fee(self, patient_id):
        pass
