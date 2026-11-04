from src.doctor import Doctor
from src.lecturer import Lecturer


class MedicalLecturer(Doctor, Lecturer):
    def __init__(self, name, person_id, module_name):
        Doctor.__init__(self, name, person_id)
        Lecturer.__init__(self, module_name)

    def role(self):
        return "Doctor"

    def fee(self):
        return super().fee()
