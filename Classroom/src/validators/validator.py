class ValidationError(Exception):
    def __init__(self, msg):
        self._msg = msg

class Validation:
    def validate_student(self, student_id, name):
        '''
        Validates the given id and name for a student
        :param student_id: The given student id (str)
        :param name: The given student name (str)
        :return: -
        '''
        self.validate_student_name(name)
        self.validate_id(student_id)

    def validate_discipline(self, discipline_id):
        '''
        Validates the given id for a discipline
        :param discipline_id: The given discipline id (str)
        :return: -
        '''
        self.validate_id(discipline_id)

    def validate_student_name(self, name):
        '''
        Checks if the given name contains any other characters than letters
        :param name: The given name (str)
        :return: -
        Raises ValidationError if the name contains anything other than letters
        '''
        for l in name:
            if not ('a' <= l <= 'z' or 'A' <= l <= 'Z' or l == ' '):
                raise ValidationError('\nName can contain only letters\n')

    def validate_grade_value(self, grade_value):
        '''
        Checks if the given grade is a number and it's in between 1 and 10
        :param grade_value: The given grade (str)
        :return: -
        Raises ValidationError if the grade is not an integer or if it is not between 1 and 10
        '''
        for i in grade_value:
            if not ('0' <= i <= '9'):
                raise ValidationError('\nGrade must be an integer\n')
        if 0 >= int(grade_value) or 10 < int(grade_value):
            raise ValidationError('\nGrade must be between 1 and 10\n')

    def validate_id(self, Id):
        '''
        Checks if the id contains only numbers and has exactly 5 characters
        :param Id: The given id (str)
        :return: -
        Raises ValidationError if the given id doesn't contain only numbers or it's length is not 5
        '''
        if len(Id) != 5:
            raise ValidationError('\nId must be of length 5\n')
        for i in Id:
            if not ('0' <= i <= '9'):
                raise ValidationError('\nId must contain only digits\n')
