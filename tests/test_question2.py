from src.patient import Patient

patient = Patient("Rutendo", 101)

print(patient.name)
print(patient.person_id)
print(patient.role())

# Test 1: Empty name
try:
    Patient("", 102)
except ValueError as error:
    print("Empty name rejected:", error)


# Test 2: Zero ID
try:
    Patient("Mary", 0)
except ValueError as error:
    print("Invalid ID rejected:", error)
    from src.clinic import Clinic

clinic = Clinic("City Medical Centre")

print(clinic.name)
print(clinic.appointments)

# Try to modify the returned appointments
try:
    clinic.appointments.append("Appointment 1")
except AttributeError:
    print("Appointments collection is protected!")