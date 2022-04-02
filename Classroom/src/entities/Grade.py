class Grade:

    def __init__(self, grade_id, discipline_id, student_id, grade_value):
        self._grade_id = grade_id
        self._discipline_id = discipline_id
        self._student_id = student_id
        self.grade_value = grade_value

    @property
    def id(self):
        return self._grade_id

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def student_id(self):
        return self._student_id

    @property
    def grade_value(self):
        return self._grade_value

    @grade_value.setter
    def grade_value(self, value):
        self._grade_value = value

    def __str__(self):
        return self._student_id + '                ' + self._discipline_id + '                    ' + str(self._grade_value)

    @classmethod
    def from_json(cls, json_list):
        return cls(*json_list)