
class Appointment:

    def __init__(self, appointment_id, patient, staff, start_hour):
        self._appointment_id = appointment_id
        self._patient = patient
        self._staff = staff
        self._start_hour = start_hour
        self._duration = 1
