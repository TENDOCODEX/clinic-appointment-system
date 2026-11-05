from src.doctor import Doctor
from src.lecturer import Lecturer


class MedicalLecturer(Doctor, Lecturer):

    def __init__(self, name, person_id, module_name):
        Doctor.__init__(self, name, person_id)
        Lecturer.__init__(self, module_name)

    def role(self):
        return "Doctor and Lecturer"

    def fee(self, patient_id=None):
        if patient_id is None:
            patient_id = self.person_id

        return super().fee(patient_id)