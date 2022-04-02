from src.validators.validator import ValidationError

class StudentRepository:
    def __init__(self):
        '''
        Creates a list for the students on initialisation
        '''
        self._student_list = []

    def __len__(self):
        return len(self._student_list)

    def add(self, student):
        '''
        Adds the given student to the student list
        :param student: The given student (Student object)
        :return: -
        Raises ValidationError if a student with the same id is already in the list
        '''
        if student.id in [stud.id for stud in self._student_list]:
            raise ValidationError('\nStudent with given id is already in data base\n')
        self._student_list.append(student)

    def __getitem__(self, given_id):
        '''
        Returns the student found with the given id
        :param given_id: The given student id (str)
        :return: The student found with the given id
        Raises ValidationError if no student was found
        '''
        if not (given_id in [stud.id for stud in self._student_list]):
            raise ValidationError('\nStudent with given id not found\n')
        for student in self._student_list:
            if student.id == given_id:
                return student

    def remove(self, student):
        self._student_list.pop(self._student_list.index(student))

    def get_id_list(self):
        return [student.id for student in self._student_list]

    def modify(self, student, new_name):
        student.name = new_name

    def search(self, search_str):
        '''
        Returns a list of all students found containing the given string in their id or name
        :param search_str: The given string (str)
        :return: The found list of students
        Raises ValidationError if no student was found
        '''
        found_list = []
        for student in self._student_list:
            if search_str.lower() in student.id or search_str.lower() in student.name.lower():
                found_list.append(student)
        if found_list == []:
            raise ValidationError('\nNo student found\n')
        return found_list
