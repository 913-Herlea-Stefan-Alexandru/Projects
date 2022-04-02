class Discipline:

    def __init__(self, discipline_id, name):
        self._discipline_id = discipline_id
        self._name = name

    @property
    def id(self):
        return self._discipline_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return self._discipline_id + '     ' + self._name.ljust(20)

    @classmethod
    def from_json(cls, json_list):
        return cls(*json_list)