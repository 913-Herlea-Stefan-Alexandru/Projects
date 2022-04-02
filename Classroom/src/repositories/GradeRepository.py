from src.validators.validator import ValidationError
from src.repositories.DisciplineRepository import DisciplineRepository
from src.repositories.StudentRepository import StudentRepository

class GradeRepository:
    def __init__(self):
        '''
        Creates a list for the grades on initialisation
        '''
        self._grade_list = []

    def list_all(self):
        return self._grade_list.copy()

    def __len__(self):
        return len(self._grade_list)

    def add(self, grade):
        self._grade_list.append(grade)

    def get_by_student(self, given_student_id):
        '''
        Returns the list of found grades for the student with the given id
        :param given_student_id: The given student id (str)
        :return: The list of found grades for the student with the given id or None if no grade was found
        '''
        found_list = []
        for grade in self._grade_list:
            if grade.student_id == given_student_id:
                found_list.append(grade)
        return found_list

    def get_by_discipline(self, given_discipline_id):
        '''
        Returns the list of found grades for the discipline with the given id
        :param given_discipline_id: The given discipline id (str)
        :return: The list of found grades for the discipline with the given id or None if no grade was found
        '''
        found_list = []
        for grade in self._grade_list:
            if grade.discipline_id == given_discipline_id:
                found_list.append(grade)
        return found_list

    def get_by_stud_disc(self, item):
        found_list = []
        discipline_id = item[:5]
        student_id = item[5:]
        for grade in self._grade_list:
            if grade.discipline_id == discipline_id and grade.student_id == student_id:
                found_list.append(grade)
        return found_list

    def remove(self, grade):
        self._grade_list.pop(self._grade_list.index(grade))