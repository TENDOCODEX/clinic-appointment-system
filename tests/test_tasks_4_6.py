import io
import unittest
from unittest.mock import patch

from src.appointment import Appointment
from src.clinic import Clinic
from src.doctor import Doctor
from src.lecturer import Lecturer
from src.medical_lecturer import MedicalLecturer
from src.nurse import Nurse
from src.patient import Patient
from src.pharmacist import Pharmacist


class Tasks456Tests(unittest.TestCase):
    def test_clinic_logging_and_failed_action_logging(self):
        clinic = Clinic("Test Clinic")
        buf = io.StringIO()

        with patch.object(clinic._Clinic__log.handlers[0], "stream", buf):
            clinic.open_log()
            clinic.add_appointment(Appointment(1, Patient("A", 10), Doctor("Dr X", 20), 9))
            try:
                clinic.add_appointment("bad")
            except ValueError:
                pass
            clinic.close_log()

        out = buf.getvalue()
        self.assertIn("opened", out.lower())
        self.assertIn("closed", out.lower())
        self.assertIn("FAILED", out.upper())

    def test_medical_lecturer_inherits_doctor_and_lecturer(self):
        before = getattr(Patient, "_constructed_count", 0)
        lecturer = MedicalLecturer("Dr Lee", 77, "Surgery")
        after = getattr(Patient, "_constructed_count", 0)
        self.assertTrue(isinstance(lecturer, Doctor))
        self.assertTrue(isinstance(lecturer, Lecturer))
        self.assertEqual(lecturer.role(), "Doctor and Lecturer")
        self.assertEqual(lecturer.module_name, "Surgery")
        self.assertEqual(lecturer.fee(), 40 + 5 * (77 % 5))
        self.assertEqual(after - before, 1)

    def test_clinic_forces_unique_and_buffer_rules(self):
        clinic = Clinic("Test Clinic")
        patient_a = Patient("A", 11)
        patient_b = Patient("B", 12, "staff_member")
        doctor = Doctor("Dr S", 21)

        clinic.add_appointment(Appointment(1, patient_a, doctor, 10))

        with self.assertRaises(ValueError):
            clinic.add_appointment(Appointment(1, patient_b, doctor, 11))

        with self.assertRaises(ValueError):
            clinic.add_appointment(Appointment(2, patient_a, doctor, 10))

        nurse = Nurse("Nurse A", 22)
        with self.assertRaises(ValueError):
            clinic.add_appointment(Appointment(3, patient_a, nurse, 10))

        # waiting list and discount logic
        clinic.add_waiting_patient(patient_b, doctor, 9)
        self.assertEqual(clinic.calculate_fee(patient_b, doctor), 0)


if __name__ == "__main__":
    unittest.main()
