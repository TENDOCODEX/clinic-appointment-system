import unittest

from src.doctor import Doctor
from src.nurse import Nurse
from src.pharmacist import Pharmacist


class TestStaffFees(unittest.TestCase):

    def setUp(self):
        self.doctor = Doctor("Dr Smith", 201)
        self.nurse = Nurse("Nurse Jane", 202)
        self.pharmacist = Pharmacist("Pharmacist John", 203)

    def test_doctor_fee(self):
        self.assertEqual(self.doctor.fee(101), 45)

    def test_nurse_fee(self):
        self.assertEqual(self.nurse.fee(101), 12)

    def test_pharmacist_fee(self):
        self.assertEqual(self.pharmacist.fee(101), 5)

    def test_fees_change_with_patient_id(self):
        self.assertEqual(self.doctor.fee(7), 50)
        self.assertEqual(self.nurse.fee(7), 11)
        self.assertEqual(self.pharmacist.fee(7), 5)


if __name__ == "__main__":
    unittest.main()