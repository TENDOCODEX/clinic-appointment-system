
import logging

from src.appointment import Appointment, AppointmentStatus


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
            handler.setFormatter(
                logging.Formatter(
                    '%(asctime)s - %(levelname)s - %(message)s'
                )
            )
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

        self.__log.info("[LOG] closed")
        self.__closed = True
        self.__opened = False

    def add_waiting_patient(self, patient, staff, start_hour):
        if not patient or not staff:
            raise ValueError("Patient and staff are required")

        self.__waiting_list.append({
            "patient": patient,
            "staff": staff,
            "start_hour": start_hour
        })

        self.__log.info(
            "[LOG] waiting patient queued for %s at hour %s",
            patient.name,
            start_hour
        )

    def calculate_fee(self, patient, staff):
        fee = staff.fee(patient.person_id)
        return fee * patient.discount_rate()

    def add_appointment(self, appointment):
        if not isinstance(appointment, Appointment):
            self.__log.warning("[FAILED] Invalid appointment object")
            raise ValueError("A valid Appointment object is required")

        appointment_id = appointment.appointment_id

        if (
            isinstance(appointment_id, bool)
            or not isinstance(appointment_id, int)
            or appointment_id <= 0
        ):
            self.__log.warning(
                "[FAILED] Invalid appointment ID %s",
                appointment_id
            )
            raise ValueError("Invalid appointment ID")

        # Check for duplicate appointment IDs
        for existing in self.__appointments:
            if existing.appointment_id == appointment_id:
                self.__log.warning(
                    "[FAILED] Duplicate appointment ID %s",
                    appointment_id
                )
                raise ValueError("Appointment ID already exists")

        emergency = appointment.patient.person_id % 4 == 1
        appointment_to_bump = None

        if emergency:
            for existing in self.__appointments:
                if (
                    existing.staff.person_id == appointment.staff.person_id
                    and existing.start_hour == appointment.start_hour
                    and existing.status != AppointmentStatus.CANCELLED
                ):
                    if existing.status == AppointmentStatus.CONFIRMED:
                        self.__log.warning(
                            "[FAILED] Emergency appointment rejected: "
                            "confirmed appointment %s cannot be bumped",
                            existing.appointment_id
                        )
                        raise ValueError(
                            "Confirmed appointments cannot be bumped"
                        )
                    appointment_to_bump = existing
                    break

        # A patient cannot have two appointments at the same hour
        for existing in self.__appointments:
            if (
                existing.patient.person_id == appointment.patient.person_id
                and existing.start_hour == appointment.start_hour
            ):
                self.__log.warning(
                    "[FAILED] Same patient already booked at hour %s",
                    appointment.start_hour
                )
                raise ValueError(
                    "A patient cannot have two appointments at the same hour"
                )

        # Enforce the staff member's required gap between appointments
        for existing in self.__appointments:
            if existing is appointment_to_bump:
                continue
            if (
                existing.staff.person_id == appointment.staff.person_id
                and abs(
                    existing.start_hour - appointment.start_hour
                ) < appointment.staff.gap_hours
            ):
                self.__log.warning(
                    "[FAILED] Staff gap rule broken for %s",
                    appointment.staff.name
                )
                raise ValueError("Staff gap rule broken")

        if appointment_to_bump is not None:
            appointment_to_bump.bump()
            self.__log.info(
                "[LOG] appointment %s bumped by emergency appointment %s",
                appointment_to_bump.appointment_id,
                appointment.appointment_id
            )

        self.__appointments.append(appointment)

        self.__log.info(
            "[LOG] appointment added for %s at %s",
            appointment.patient.name,
            appointment.start_hour
        )

