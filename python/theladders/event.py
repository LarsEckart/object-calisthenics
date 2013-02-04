# Use unix epoch time for now

class Event:
    def __init__(self, time):
        self.time = time

    def in_range(self, start, end):
        return self.time > start and self.time < end
