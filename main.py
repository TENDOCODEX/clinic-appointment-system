from src.appointment import Appointment
from src.clinic import Clinic
from src.doctor import Doctor
from src.medical_lecturer import MedicalLecturer
from src.nurse import Nurse
from src.patient import Patient
from src.pharmacist import Pharmacist


class DemoClock:
    def __init__(self, current_hour):
        self.current_hour = current_hour

    def now(self):
        return self.current_hour


def main():
    clinic = Clinic("City Medical Centre")
    clinic.open_log()

    student = Patient("Rutendo", 102, "student")
    staff_patient = Patient("Tariro", 103, "staff_member")
    visitor = Patient("Farai", 104)
    pending_patient = Patient("Kuda", 106)
    confirmed_patient = Patient("Nyasha", 107)
    emergency_patient = Patient("Emergency One", 201)
    second_emergency_patient = Patient("Emergency Two", 205)

    doctor = Doctor("Dr Smith", 201)
    nurse = Nurse("Nurse Jane", 202)
    pharmacist = Pharmacist("Pharmacist John", 203)

    print("\nPATIENTS AND STAFF")
    for patient in (student, staff_patient, visitor):
        print(f"{patient.name} (ID {patient.person_id}, {patient.patient_type})")
    for staff in (doctor, nurse, pharmacist):
        print(f"{staff.role()}: {staff.name}")

    print("\nSTAFF FEES")
    for staff in (doctor, nurse, pharmacist):
        print(f"{staff.role()}: ${staff.fee(student.person_id)}")
    lecturer = MedicalLecturer("Dr Lee", 77, "Surgery")
    print(
        f"{lecturer.role()} ({lecturer.module_name}): "
        f"${lecturer.fee(student.person_id)}"
    )
    print(f"Discounted clinic fee for student with doctor: ${clinic.calculate_fee(student, doctor)}")

    print("\nBOOK, CONFIRM AND CANCEL")
    appointment = Appointment(1, student, doctor, 8)
    clinic.add_appointment(appointment)
    appointment.confirm()
    print(f"Appointment {appointment.appointment_id}: {appointment.status.value}")
    appointment.cancel(DemoClock(6))
    print(f"Appointment {appointment.appointment_id}: {appointment.status.value}")

    print("\nINVALID INPUT AND SCHEDULING CONFLICTS")
    try:
        Appointment(2, student, doctor, 169)
    except ValueError as error:
        print(f"Invalid appointment rejected: {error}")

    try:
        clinic.add_appointment(Appointment(2, student, doctor, 8))
    except ValueError as error:
        print(f"Patient scheduling conflict rejected: {error}")

    try:
        clinic.add_appointment(Appointment(3, staff_patient, doctor, 9))
    except ValueError as error:
        print(f"Staff buffer conflict rejected: {error}")

    print("\nEMERGENCY BUMP OF PENDING APPOINTMENT")
    pending = Appointment(4, pending_patient, doctor, 20)
    clinic.add_appointment(pending)
    emergency = Appointment(5, emergency_patient, doctor, 20)
    clinic.add_appointment(emergency)
    print(
        f"Appointment {pending.appointment_id}: {pending.status.value}, "
        f"reason={pending.cancellation_reason}"
    )
    print(f"Appointment {emergency.appointment_id}: {emergency.status.value}")

    print("\nCONFIRMED APPOINTMENT CANNOT BE BUMPED")
    confirmed = Appointment(6, confirmed_patient, doctor, 30)
    clinic.add_appointment(confirmed)
    confirmed.confirm()
    try:
        clinic.add_appointment(
            Appointment(7, second_emergency_patient, doctor, 30)
        )
    except ValueError as error:
        print(f"Emergency booking rejected: {error}")
    print(f"Appointment {confirmed.appointment_id}: {confirmed.status.value}")

    clinic.close_log()


if __name__ == "__main__":
    main()
