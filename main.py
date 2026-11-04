from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment
from src.clinic import Clinic

patient = Patient("Rutendo", 101)
doctor = Doctor("Dr Smith", 201)

appointment = Appointment(1, patient, doctor, 10)

clinic = Clinic("City Medical Centre")

clinic.add_appointment(appointment)

print(clinic.name)
print(len(clinic.appointments))