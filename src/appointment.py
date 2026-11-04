from src.patient import Patient
from src.staff import Staff
from enum import Enum


class AppointmentStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


# Appointment invariants:
# 1. Appointment ID must be a positive integer.
# 2. Patient and staff must be valid objects.
# 3. Start hour must be a whole number between 0 and 168.
# 4. Every appointment lasts exactly one hour.
# 5. Status must always be PENDING, CONFIRMED or CANCELLED.
# 6. A CANCELLED appointment can never become active again.
# 7. An appointment cannot be cancelled after it has started.


class Appointment:

    def __init__(self, appointment_id, patient, staff, start_hour):

        if isinstance(appointment_id, bool) or not isinstance(appointment_id, int) or appointment_id <= 0:
            raise ValueError("Appointment ID must be a positive integer")

        if not isinstance(patient, Patient):
            raise ValueError("A valid Patient object is required")

        if not isinstance(staff, Staff):
            raise ValueError("A valid Staff object is required")

        if isinstance(start_hour, bool) or not isinstance(start_hour, int) or not 0 <= start_hour <= 168:
            raise ValueError("Start hour must be between 0 and 168")

        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__staff = staff
        self.__start_hour = start_hour
        self.__duration = 1
        self.__status = AppointmentStatus.PENDING

    @property
    def appointment_id(self):
        return self.__appointment_id

    @property
    def patient(self):
        return self.__patient

    @property
    def staff(self):
        return self.__staff

    @property
    def start_hour(self):
        return self.__start_hour

    @property
    def duration(self):
        return self.__duration

    @property
    def status(self):
        return self.__status

    def confirm(self):
        if self.__status != AppointmentStatus.PENDING:
            raise ValueError("Only pending appointments can be confirmed")

        self.__status = AppointmentStatus.CONFIRMED

    def cancel(self, clock):
        if self.__status == AppointmentStatus.CANCELLED:
            raise ValueError("Cancelled appointments cannot be changed")

        current_hour = clock.now()

        if current_hour >= self.__start_hour:
            raise ValueError("Appointment has already started")

        if self.__status == AppointmentStatus.CONFIRMED:
            if self.__start_hour - current_hour < 2:
                raise ValueError("Confirmed appointments cannot be cancelled less than 2 hours before start")

        self.__status = AppointmentStatus.CANCELLED