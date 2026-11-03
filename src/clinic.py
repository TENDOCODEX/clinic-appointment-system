
# Clinic invariants:
# 1. The clinic must have a non-empty name.
# 2. Every stored appointment must have a valid appointment ID.
# 3. Appointment IDs must be unique within the clinic.
# 4. The internal appointments list must never be exposed directly.

from src.appointment import Appointment


class Clinic:

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Clinic name cannot be empty")

        self.__name = name.strip()
        self.__appointments = []

    @property
    def name(self):
        return self.__name

    @property
    def appointments(self):
        return tuple(self.__appointments)

    def add_appointment(self, appointment):
        if not isinstance(appointment, Appointment):
            raise ValueError("A valid Appointment object is required")

        appointment_id = appointment.appointment_id

        if (isinstance(appointment_id, bool)
                or not isinstance(appointment_id, int)
                or appointment_id <= 0):
            raise ValueError("Invalid appointment ID")

        for existing in self.__appointments:
            if existing.appointment_id == appointment_id:
                raise ValueError("Appointment ID already exists")

        self.__appointments.append(appointment)
