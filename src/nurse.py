
from src.staff import Staff


class Nurse(Staff):

    @property
    def gap_hours(self):
        return 1

    def role(self):
        return "Nurse"

    def fee(self, patient_id):
        return 10 + (patient_id % 3)
