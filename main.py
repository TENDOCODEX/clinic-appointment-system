from src.patient import Patient
from src.doctor import Doctor
from src.nurse import Nurse
from src.pharmacist import Pharmacist

patient = Patient("Rutendo", 101)

staff_members = [
    Doctor("Dr Smith", 201),
    Nurse("Nurse Jane", 202),
    Pharmacist("Pharmacist John", 203)
]

print("PATIENT:", patient.name)
print("PATIENT ID:", patient.person_id)

print("\nSTAFF FEES")

for staff in staff_members:
    print(f"Role: {staff.role()}")
    print(f"Fee: ${staff.fee(patient.person_id)}")
    print("-------------------")