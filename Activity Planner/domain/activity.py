

class Activity:
    def __init__(self, name, duration):
        self._name = name
        self._duration = duration

    @property
    def name(self):
        return self._name

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        return self._name
