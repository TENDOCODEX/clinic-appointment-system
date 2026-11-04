class TestClock:

    def __init__(self, current_hour):
        self.current_hour = current_hour

    def now(self):
        return self.current_hour