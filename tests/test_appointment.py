from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment, AppointmentStatus

patient = Patient("Rutendo", 101)
doctor = Doctor("Dr Smith", 201)

appointment = Appointment(1, patient, doctor, 10)

print("Appointment ID:", appointment.appointment_id)
print("Patient:", appointment.patient.name)
print("Staff:", appointment.staff.name)
print("Start hour:", appointment.start_hour)
print("Duration:", appointment.duration)
print("Status:", appointment.status.value)
from tests.test_clock import TestClock

# Test 1: Confirm a pending appointment
appointment.confirm()
print("After confirmation:", appointment.status.value)

# Test 2: Cancel a confirmed appointment exactly 2 hours before
clock = TestClock(8)
appointment.cancel(clock)
print("After cancellation:", appointment.status.value)
# Test 3: Cancellation less than 2 hours before start
appointment2 = Appointment(2, patient, doctor, 10)
appointment2.confirm()

clock2 = TestClock(9)

try:
    appointment2.cancel(clock2)
except ValueError as error:
    print("Cancellation rejected:", error)

print("Appointment status:", appointment2.status.value)
# Test 4: A cancelled appointment cannot be confirmed again
try:
    appointment.confirm()
except ValueError as error:
    print("Reconfirmation rejected:", error)


# Test 5: A cancelled appointment cannot be cancelled again
try:
    appointment.cancel(TestClock(7))
except ValueError as error:
    print("Repeated cancellation rejected:", error)


# Test 6: Cannot cancel an appointment that has already started
appointment3 = Appointment(3, patient, doctor, 10)

try:
    appointment3.cancel(TestClock(10))
except ValueError as error:
    print("Cancellation after start rejected:", error)

print("Appointment 3 status:", appointment3.status.value)


# Test private appointment fields
try:
    appointment.appointment_id = 99
except AttributeError:
    print("Appointment ID is protected!")

try:
    appointment.start_hour = 15
except AttributeError:
    print("Appointment start hour is protected!")

try:
    appointment.status = AppointmentStatus.CANCELLED
except AttributeError:
    print("Appointment status is protected!")
    # Test invalid patient
try:
    Appointment(4, "Rutendo", doctor, 12)
except ValueError as error:
    print("Invalid patient rejected:", error)


# Test invalid staff
try:
    Appointment(5, patient, "Dr Smith", 12)
except ValueError as error:
    print("Invalid staff rejected:", error)