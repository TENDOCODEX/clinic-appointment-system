
from src.clinic import Clinic
from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment

clinic = Clinic("City Medical Centre")

patient = Patient("Rutendo", 101)
doctor = Doctor("Dr Smith", 201)

appointment1 = Appointment(1, patient, doctor, 10)

# Test adding a valid appointment
clinic.add_appointment(appointment1)
print("Appointments:", len(clinic.appointments))

# Test duplicate appointment ID
appointment2 = Appointment(1, patient, doctor, 12)

try:
    clinic.add_appointment(appointment2)
except ValueError as error:
    print("Duplicate rejected:", error)

print("Final appointments:", len(clinic.appointments))
# Test 1: Cannot directly modify the clinic name
try:
    clinic.name = "New Clinic"
except AttributeError:
    print("Clinic name is protected!")


# Test 2: Cannot append to the returned appointments collection
try:
    clinic.appointments.append(appointment2)
except AttributeError:
    print("Appointments collection is protected!")


# Test 3: Confirm the original appointment remains
print("Appointments after protection tests:", len(clinic.appointments))

# Test invalid appointment object
try:
    clinic.add_appointment("Not an appointment")
except ValueError as error:
    print("Invalid appointment rejected:", error)