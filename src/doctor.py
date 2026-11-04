
from src.staff import Staff


class Doctor(Staff):

    @property
    def gap_hours(self):
        return 2

    def role(self):
        return "Doctor"

    def fee(self):
        return 40
