from src.staff import Staff


class Pharmacist(Staff):

    @property
    def gap_hours(self):
        return 0

    def role(self):
        return "Pharmacist"

    def fee(self, patient_id):
        return 5
