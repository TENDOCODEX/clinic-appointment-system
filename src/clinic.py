
# Clinic invariants:
# 1. The clinic must have a non-empty name.
# 2. Every stored appointment must have a valid appointment ID.
# 3. Appointment IDs must be unique within the clinic.
# 4. The internal appointments list must never be exposed directly.

import logging

from src.appointment import Appointment


class Clinic:

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Clinic name cannot be empty")

        self.__name = name.strip()
        self.__appointments = []
        self.__waiting_list = []
        self.__log = logging.getLogger(__name__)
        self.__log.setLevel(logging.INFO)
        if not self.__log.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self.__log.addHandler(handler)
        self.__opened = False
        self.__closed = False

    @property
    def name(self):
        return self.__name

    @property
    def appointments(self):
        return tuple(self.__appointments)

    @property
    def waiting_list(self):
        return tuple(self.__waiting_list)

    def open_log(self):
        if self.__opened:
            raise ValueError("Clinic is already open")
        self.__opened = True
        self.__closed = False
        self.__log.info("[LOG] opened")

    def close_log(self):
        if not self.__opened or self.__closed:
            raise ValueError("Clinic is not open")
        self.__closed = True
        self.__opened = False
        self.__log.info("[LOG] closed")

    def add_waiting_patient(self, patient, staff, start_hour):
        if not patient or not staff:
            raise ValueError("Patient and staff are required")
        self.__waiting_list.append({"patient": patient, "staff": staff, "start_hour": start_hour})
        self.__log.info("[LOG] waiting patient queued for %s at hour %s", patient.name, start_hour)

    def calculate_fee(self, patient, staff):
        fee = staff.fee()
        if getattr(patient, "patient_type", "visitor") == "student":
            return fee * 0.5
        if getattr(patient, "patient_type", "visitor") == "staff_member":
            return fee * 0.0
        return fee

    def add_appointment(self, appointment):
        if not isinstance(appointment, Appointment):
            self.__log.warning("[FAILED] Invalid appointment object")
            raise ValueError("A valid Appointment object is required")

        appointment_id = appointment.appointment_id

        if (isinstance(appointment_id, bool)
                or not isinstance(appointment_id, int)
                or appointment_id <= 0):
            self.__log.warning("[FAILED] Invalid appointment ID %s", appointment_id)
            raise ValueError("Invalid appointment ID")

        for existing in self.__appointments:
            if existing.appointment_id == appointment_id:
                self.__log.warning("[FAILED] Duplicate appointment ID %s", appointment_id)
                raise ValueError("Appointment ID already exists")

        for existing in self.__appointments:
            if existing.patient.person_id == appointment.patient.person_id and existing.start_hour == appointment.start_hour:
                self.__log.warning("[FAILED] Same patient already booked at hour %s", appointment.start_hour)
                raise ValueError("A patient cannot have two appointments at the same hour")

        if appointment.staff is not None:
            for existing in self.__appointments:
                if existing.staff.person_id == appointment.staff.person_id and abs(existing.start_hour - appointment.start_hour) < getattr(appointment.staff, 'gap_hours', 0):
                    self.__log.warning("[FAILED] Staff gap rule broken for %s", appointment.staff.name)
                    raise ValueError("Staff gap rule broken")

        self.__appointments.append(appointment)
        self.__log.info("[LOG] appointment added for %s at %s", appointment.patient.name, appointment.start_hour)
