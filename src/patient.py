
from src.person import Person


class Patient(Person):

    def __init__(self, name, person_id, patient_type="visitor"):
        super().__init__(name, person_id)
        valid_types = {"student", "staff_member", "visitor"}
        if patient_type not in valid_types:
            raise ValueError("Patient type must be student, staff_member or visitor")
        self._patient_type = patient_type

    @property
    def patient_type(self):
        return self._patient_type

    def discount_rate(self):
        rates = {"student": 0.5, "staff_member": 0.0, "visitor": 1.0}
        return rates[self._patient_type]

    def role(self):
        return "Patient"
