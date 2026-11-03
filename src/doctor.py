
from src.staff import Staff


class Doctor(Staff):

    def role(self):
        return "Doctor"

    def fee(self):
        return 40
