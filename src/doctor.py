
from src.staff import Staff


class Doctor(Staff):

    @property
    def gap_hours(self):
        return 2

    def role(self):
        return "Doctor"

    def fee(self, patient_id):
        return 40 + 5 * (patient_id % 5)
