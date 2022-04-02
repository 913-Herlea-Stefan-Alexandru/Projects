from src.entities.Student import Student
from src.entities.Discipline import Discipline
from src.entities.Grade import Grade
from src.services.undoService import FunctionCall, Operation, CascadeOperations
from src.validators.validator import ValidationError
from src.entities.IterableStructure import sort, filter

class Service:
    def __init__(self, student_repo, discipline_repo, grade_repo, validator, undo_service):
        '''
        Initialise the service class with the given repositories
        :param student_repo: The student repository (StudentRepository object)
        :param discipline_repo: The discipline repository (DisciplineRepository object)
        :param grade_repo: The grade repository (GradeRepository object)
        :param validator: The validator (Validation object)
        '''
        self._validator = validator
        self._student_repo = student_repo
        self._discipline_repo = discipline_repo
        self._grade_repo = grade_repo
        self._undo_service = undo_service

    def add_student(self, student_id, name):
        '''
        Validates the given parameters and creates and adds a student to the student repo
        :param student_id: The student id (str)
        :param name: The student name (str)
        :return: -
        '''
        self._validator.validate_student(student_id, name)
        student = Student(student_id, name)
        self._student_repo.add(student)

        undo_func = FunctionCall(self._student_repo.remove, student)
        redo_func = FunctionCall(self._student_repo.add, student)
        op = Operation(undo_func, redo_func)
        self._undo_service.record(op)

    def list_all_students(self):
        '''
        Gets a list of all students from the student repo and returns it
        :return: The list of students from the student repo (list of Student objects)
        '''
        student_list = []
        for student_id in self._student_repo.get_id_list():
            student_list.append(self._student_repo[student_id])
        return student_list

    def remove_student(self, student_id):
        '''
        Validates the given id and removes the student and it's grades from the respective repositories
        :param student_id: The student id (str)
        :return: -
        '''
        self._validator.validate_id(student_id)
        student = self._student_repo[student_id]
        self._student_repo.remove(student)

        undo_func = FunctionCall(self._student_repo.add, student)
        redo_func = FunctionCall(self._student_repo.remove, student)

        op = Operation(undo_func, redo_func)

        cascade_list = [op]

        found_grade_list = self._grade_repo.get_by_student(student_id)
        for grade in found_grade_list:
            self._grade_repo.remove(grade)
            undo_func = FunctionCall(self._grade_repo.add, grade)
            redo_func = FunctionCall(self._grade_repo.remove, grade)
            cascade_list.append(Operation(undo_func, redo_func))

        self._undo_service.record(CascadeOperations(*cascade_list))

    def update_student(self, student_id, new_name):
        '''
        Validates the given parameters and changes the name of the student with the given id with the given name
        :param student_id: The student id (str)
        :param new_name: The new student name (str)
        :return: -
        '''
        self._validator.validate_student(student_id, new_name)
        student = self._student_repo[student_id]
        old_name = student.name
        self._student_repo.modify(student, new_name)

        undo_func = FunctionCall(self._student_repo.modify, student, old_name)
        redo_func = FunctionCall(self._student_repo.modify, student, new_name)
        op = Operation(undo_func, redo_func)
        self._undo_service.record(op)


    def add_discipline(self, discipline_id, name):
        '''
        Validates the given parameters and creates and adds a discipline to the discipline repo
        :param discipline_id: The discipline id (str)
        :param name: The discipline name (str)
        :return: -
        '''
        self._validator.validate_discipline(discipline_id)
        discipline = Discipline(discipline_id, name)
        self._discipline_repo.add(discipline)

        undo_func = FunctionCall(self._discipline_repo.remove, discipline)
        redo_func = FunctionCall(self._discipline_repo.add, discipline)
        op = Operation(undo_func, redo_func)
        self._undo_service.record(op)

    def list_all_disciplines(self):
        '''
        Gets a list of all disciplines from the discipline repo and returns it
        :return: The list of all disciplines (list of Discipline objects)
        '''
        discipline_list = []
        for discipline_id in self._discipline_repo.get_id_list():
            discipline_list.append(self._discipline_repo[discipline_id])
        return discipline_list

    def remove_discipline(self, discipline_id):
        '''
        Validates the given id and removes the discipline and it's grades from the respective repositories
        :param discipline_id: The discipline id (str)
        :return: -
        '''
        self._validator.validate_id(discipline_id)
        discipline = self._discipline_repo[discipline_id]
        self._discipline_repo.remove(discipline)

        undo_func = FunctionCall(self._discipline_repo.add, discipline)
        redo_func = FunctionCall(self._discipline_repo.remove, discipline)

        op = Operation(undo_func, redo_func)

        cascade_list = [op]

        found_grade_list = self._grade_repo.get_by_discipline(discipline_id)
        for grade in found_grade_list:
            self._grade_repo.remove(grade)
            undo_func = FunctionCall(self._grade_repo.add, grade)
            redo_func = FunctionCall(self._grade_repo.remove, grade)
            cascade_list.append(Operation(undo_func, redo_func))

        self._undo_service.record(CascadeOperations(*cascade_list))


    def update_discipline(self, discipline_id, new_name):
        '''
        Validates the given parameters and changes the name of the discipline with the given id with the given name
        :param discipline_id: The discipline id (str)
        :param new_name: The new discipline name (str)
        :return: -
        '''
        self._validator.validate_discipline(discipline_id)
        discipline = self._discipline_repo[discipline_id]
        old_name = discipline.name
        self._discipline_repo.modify(discipline, new_name)

        undo_func = FunctionCall(self._discipline_repo.modify, discipline, old_name)
        redo_func = FunctionCall(self._discipline_repo.modify, discipline, new_name)
        op = Operation(undo_func, redo_func)
        self._undo_service.record(op)

    def add_grade(self, grade_id, discipline_id, student_id, grade_value):
        '''
        Validates the given parameters and creates and adds a grade to the grade repo
        :param discipline_id: The discipline id (str)
        :param student_id: The student id (str)
        :param grade_value: The grade value (str)
        :return: -
        '''
        self._validator.validate_grade_value(grade_value)
        grade_value = int(grade_value)
        discipline = self._discipline_repo[discipline_id]
        student = self._student_repo[student_id]
        grade = Grade(grade_id, discipline.id, student.id, grade_value)
        self._grade_repo.add(grade)

        undo_func = FunctionCall(self._grade_repo.remove, grade)
        redo_func = FunctionCall(self._grade_repo.add, grade)
        op = Operation(undo_func, redo_func)
        self._undo_service.record(op)

    def failing_students(self):
        '''
        Returns the a list of all failing students
        :return: The list of all failing students
        '''
        stud_fail = []
        for student_id in self.get_student_id_list():
            for discipline_id in self.get_discipline_id_list():
                try:
                    if self.grade_average([grade.grade_value for grade
                                           in self.find_grades_discipline_student(discipline_id, student_id)]) < 5 \
                            and self._student_repo[student_id] not in stud_fail:
                        stud_fail.append(self._student_repo[student_id])
                except ValueError:
                    pass
        return stud_fail

    def find_grades_discipline_student(self, discipline_id, student_id):
        return self._grade_repo.get_by_stud_disc(discipline_id+student_id)

    def grade_average(self, grades):
        '''
        Returns the average of the grades given as a parameter
        :param grades: The list of grades (list og Grade objects)
        :return: The average of the grades given
        Raises ValueError if the length of the grades list is 0
        '''
        if len(grades) > 0:
            s = 0
            for grade in grades:
                s += grade
            return s / len(grades)
        raise ValueError()

    def aggregated_avg_crit(self, item):
        return item.aggregated_avg

    def top_students(self):
        '''
        Returns a list sorted by the aggregated average of all students at all disciplines
        :return: A list of StudentTop objects
        '''
        top_list = []
        for student_id in self.get_student_id_list():
            avg_grades = []
            for discipline_id in self.get_discipline_id_list():
                stud_grades = self.find_grades_discipline_student(discipline_id, student_id)
                if len(stud_grades) > 0:
                    avg_grades.append(self.grade_average([grade.grade_value for grade in stud_grades]))
            if len(avg_grades) > 0:
                top_list.append(StudentTop(self._student_repo[student_id], self.grade_average(avg_grades)))
        sort(top_list, self.aggregated_avg_crit)
        # top_list.sort(reverse=True, key=(lambda a: a.aggregated_avg))
        return top_list

    def avg_crit(self, item):
        return item.avg

    def top_disciplines(self):
        '''
        Returns a list sorted by the average of the grades obtained by all students any discipline
        :return: A list of DisciplineTop objects
        '''
        top_list = []
        for discipline_id in self.get_discipline_id_list():
            grades = self._grade_repo.get_by_discipline(discipline_id)
            if len(grades) > 0:
                top_list.append(DisciplineTop(self._discipline_repo[discipline_id],
                                              self.grade_average([grade.grade_value for grade in grades])))
        sort(top_list, self.avg_crit)
        # top_list.sort(reverse=True, key=(lambda a: a.avg))
        return top_list

    def list_all_grades(self):
        '''
        Gets a list of all grades from the grade repo and returns it
        :return: The list of all grades (list of Grade objects)
        '''
        grade_list = []
        for grade_id in self._grade_repo.get_id_list():
            grade_list.append(self._grade_repo[grade_id])
        return grade_list

    def get_student_id_list(self):
        '''
        Returns all of the student ids from the student repo
        :return: All of the student ids from the student repo
        '''
        return self._student_repo.get_id_list()

    def get_discipline_id_list(self):
        '''
        Returns all of the discipline ids from the student repo
        :return: All of the discipline ids from the student repo
        '''
        return self._discipline_repo.get_id_list()

    def filter_by_string(self, item):
        if self._string in item.id or self._string in item.name.lower():
            return True
        return False

    def search_students(self, search_str):
        '''
        Searches for the students which contain the given string in their id or name and returns a list of them
        :param search_str: The given partial string (str)
        :return: The list of found students (list of Student objects)
        '''
        self._string = search_str.lower()
        array = [self._student_repo[student_id] for student_id in self.get_student_id_list()]
        array = filter(array, self.filter_by_string)
        return array

    def search_disciplines(self, search_str):
        '''
        Searches for the disciplines which contain the given string in their id or name and returns a list of them
        :param search_str: The given partial string (str)
        :return: The list of found disciplines (list of Discipline objects)
        '''
        self._string = search_str.lower()
        array = [self._discipline_repo[discipline_id] for discipline_id in self.get_discipline_id_list()]
        array = filter(array, self.filter_by_string)
        return array

    def undo(self):
        return self._undo_service.undo()

    def redo(self):
        return self._undo_service.redo()

class StudentTop:
    '''
    Objects of this class contain a student and he's aggregated average
    '''
    def __init__(self, student, aggregated_avg):
        self._student = student
        self._aggregated_avg = aggregated_avg

    @property
    def student(self):
        return self._student

    @property
    def aggregated_avg(self):
        return self._aggregated_avg

    def __str__(self):
        return str(self._student) + '  ' + str(self._aggregated_avg)

class DisciplineTop:
    '''
    Objects of this class contain a discipline and the average of the grades obtained by all students at it
    '''
    def __init__(self, discipline, avg):
        self._discipline = discipline
        self._avg = avg

    @property
    def discipline(self):
        return self._discipline

    @property
    def avg(self):
        return self._avg

    def __str__(self):
        return str(self.discipline) + '  ' + str(self.avg)