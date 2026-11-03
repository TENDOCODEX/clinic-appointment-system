
class Clinic:

    def __init__(self, name):
        self._name = name
        self._appointments = []

    def add_appointment(self, appointment):
        self._appointments.append(appointment)
