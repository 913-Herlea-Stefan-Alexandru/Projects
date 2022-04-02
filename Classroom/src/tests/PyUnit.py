import unittest
import random
import string
from src.entities.Student import Student
from src.entities.Discipline import Discipline
from src.entities.Grade import Grade
from src.validators.validator import Validation, ValidationError
from src.services.services import Service
from src.services.undoService import UndoService
from src.repositories.Repository import Repository
from src.entities.IterableStructure import Iterable

class MyTestCase(unittest.TestCase):
    def test_student(self):
        student = Student('12345', 'Gabi George')
        self.assertEqual(student.id == '12345' and student.name == 'Gabi George', True)
        student.name = 'Mihai George'
        self.assertEqual(student.name == 'Mihai George', True)
        val = Validation()
        try:
            val.validate_student('12345', 'Miha1 G3org3')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)
        try:
            val.validate_student('efef3', 'George')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)
        try:
            str(student)
            self.assertEqual(True, True)
        except:
            self.assertEqual(False, True)

    def test_discipline(self):
        discipline = Discipline('5356', 'Math')
        self.assertEqual(discipline.id == '5356' and discipline.name == 'Math', True)
        discipline.name = 'FP'
        self.assertEqual(discipline.name == 'FP', True)
        val = Validation()
        try:
            val.validate_discipline('dwqf45')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)
        try:
            str(discipline)
            self.assertEqual(True, True)
        except:
            self.assertEqual(False, True)

    def test_grade(self):
        grade = Grade('11111', '12345', '3225', 9)
        self.assertEqual(grade.discipline_id == '12345' and grade.student_id == '3225' and grade.grade_value == 9, True)
        grade.grade_value = 5
        self.assertEqual(grade.grade_value == 5, True)
        val = Validation()
        try:
            val.validate_grade_value('34')
            self.assertEqual(True, False)
        except ValidationError:
            self.assertEqual(True, True)
        try:
            val.validate_grade_value('we')
            self.assertEqual(True, False)
        except ValidationError:
            self.assertEqual(True, True)
        try:
            str(grade)
            self.assertEqual(True, True)
        except:
            self.assertEqual(False, True)

    def test_iterable(self):
        it = Iterable()
        andreea = Student('11111', 'Andreea')
        it + andreea
        stefan = Student('22222', 'Stefan')
        it + stefan
        dan = Student('33333', 'Dan')
        it + dan
        del it[2]
        self.assertEqual(it[0], andreea)
        self.assertEqual(it[1], stefan)
        self.assertEqual(len(it), 2)
        del it[None]
        self.assertEqual(len(it), 1)
        it[0] = dan
        self.assertEqual(len(it) == 1 and it[0] == dan, True)

    def test_add_student(self):
        st_repo = Repository()
        sv = Service(st_repo, Repository(), Repository(), Validation(), UndoService())
        sv.add_student('12345', 'Dan')
        self.assertEqual(len(st_repo) == 1, True)
        try:
            sv.add_student('12345', 'Bob')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)

    def test_remove_student(self):
        st_repo = Repository()
        gr_repo = Repository()
        sv = Service(st_repo, Repository(), gr_repo, Validation(), UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        sv.add_discipline('12345', 'Math')
        sv.add_grade('11111', '12345', '12345', '8')
        sv.remove_student('12345')
        self.assertEqual(len(st_repo) == 1 and len(gr_repo) == 0, True)
        try:
            sv.remove_student('12345')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)

    def test_list_all_students(self):
        st_repo = Repository()
        sv = Service(st_repo, Repository(), Repository(), Validation(), UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        student_list = sv.list_all_students()
        self.assertEqual(student_list[0].id == '12345' and student_list[1].id == '13467', True)

    def test_update_student(self):
        st_repo = Repository()
        sv = Service(st_repo, Repository(), Repository(), Validation(), UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        sv.update_student('12345', 'Bogdan')
        self.assertEqual(st_repo['12345'].name == 'Bogdan', True)
        try:
            sv.update_student('11111', 'Gog')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)

    def test_add_discipline(self):
        dc_repo = Repository()
        sv = Service(Repository(), dc_repo, Repository(), Validation(), UndoService())
        sv.add_discipline('12345', 'Math')
        self.assertEqual(len(dc_repo) == 1, True)
        try:
            sv.add_discipline('12345', 'Math2')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)

    def test_list_all_disciplines(self):
        dc_repo = Repository()
        sv = Service(Repository(), dc_repo, Repository(), Validation(), UndoService())
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        discipline_list = sv.list_all_disciplines()
        self.assertEqual(discipline_list[0].id == '12345' and discipline_list[1].id == '34567', True)

    def test_remove_discipline(self):
        dc_repo = Repository()
        gr_repo = Repository()
        sv = Service(Repository(), dc_repo, gr_repo, Validation(), UndoService())
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        sv.add_student('12345', 'Dan')
        sv.add_grade('11111', '12345', '12345', '10')
        sv.remove_discipline('12345')
        self.assertEqual(len(dc_repo) == 1 and len(gr_repo) == 0, True)
        try:
            sv.remove_discipline('12345')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)

    def test_update_discipline(self):
        dc_repo = Repository()
        sv = Service(Repository(), dc_repo, Repository(), Validation(), UndoService())
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        sv.update_discipline('12345', 'Logic')
        self.assertEqual(dc_repo['12345'].name == 'Logic', True)
        try:
            sv.update_discipline('23526', 'N')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)

    def test_add_grade(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        val = Validation()
        sv = Service(st_repo, dc_repo, gr_repo, val, UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        sv.add_grade('11111', '12345', '13467', '10')
        self.assertEqual(len(gr_repo) == 1, True)
        try:
            sv.add_grade('22222', '25235', '32425', '10')
            self.assertEqual(False, True)
        except ValidationError:
            self.assertEqual(True, True)

    def test_list_all_grades(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        val = Validation()
        sv = Service(st_repo, dc_repo, gr_repo, val, UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        sv.add_grade('11111', '12345', '13467', '10')
        grade_list = sv.list_all_grades()
        self.assertEqual(grade_list[0].student_id == '13467' and grade_list[0].discipline_id == '12345', True)

    def test_test_init(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        test_init(st_repo, dc_repo, gr_repo)

    def test_search_students(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        val = Validation()
        sv = Service(st_repo, dc_repo, gr_repo, val, UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        found_list = sv.search_students('34')
        self.assertEqual(found_list[0].id == '12345' and found_list[1].id == '13467'
                         and len(found_list) == 2, True)

    def test_search_disciplines(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        val = Validation()
        sv = Service(st_repo, dc_repo, gr_repo, val, UndoService())
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('13467', 'Arithmetics')
        found_list = sv.search_disciplines('th')
        self.assertEqual(found_list[0].id == '12345' and found_list[1].id == '13467'
                         and len(found_list) == 2, True)
        found_list = sv.search_disciplines('99')
        self.assertEqual(len(found_list), 0)

    def test_failing_students(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        val = Validation()
        sv = Service(st_repo, dc_repo, gr_repo, val, UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        sv.add_student('54321', 'Roger')
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        sv.add_grade('11111', '12345', '13467', '10')
        sv.add_grade('22222', '12345', '12345', '4')
        sv.add_grade('33333', '12345', '12345', '5')
        sv.add_grade('44444', '34567', '12345', '3')
        sv.add_grade('55555', '12345', '54321', '7')
        sv.add_grade('66666', '12345', '54321', '5')
        sv.add_grade('77777', '34567', '54321', '2')
        failing = sv.failing_students()
        self.assertEqual(failing[0].name == 'Dan' and failing[1].name == 'Roger', True)

    def test_top_students(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        val = Validation()
        sv = Service(st_repo, dc_repo, gr_repo, val, UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        sv.add_student('54321', 'Roger')
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        sv.add_grade('11111', '12345', '13467', '10')
        sv.add_grade('22222', '12345', '12345', '4')
        sv.add_grade('33333', '12345', '12345', '5')
        sv.add_grade('44444', '34567', '12345', '3')
        sv.add_grade('55555', '12345', '54321', '7')
        sv.add_grade('66666', '12345', '54321', '5')
        sv.add_grade('77777', '34567', '54321', '4')
        stud_top = sv.top_students()
        self.assertEqual(stud_top[0].student.name == 'Bob' and stud_top[1].student.name == 'Roger'
                         and stud_top[2].student.name == 'Dan', True)
        for s_t in stud_top:
            try:
                str(s_t)
                self.assertEqual(True, True)
            except:
                self.assertEqual(False, True)

    def test_top_disciplines(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        val = Validation()
        sv = Service(st_repo, dc_repo, gr_repo, val, UndoService())
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        sv.add_student('54321', 'Roger')
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        sv.add_discipline('22222', 'Algebra')
        sv.add_grade('11111', '12345', '13467', '1')
        sv.add_grade('22222', '12345', '12345', '4')
        sv.add_grade('33333', '12345', '12345', '5')
        sv.add_grade('44444', '34567', '12345', '10')
        sv.add_grade('55555', '12345', '54321', '7')
        sv.add_grade('66666', '12345', '54321', '5')
        sv.add_grade('77777', '34567', '54321', '4')
        sv.add_grade('88888', '22222', '12345', '1')
        disc_top = sv.top_disciplines()
        self.assertEqual(disc_top[0].discipline.name == 'FP' and disc_top[1].discipline.name == 'Math', True)
        for d_t in disc_top:
            try:
                str(d_t)
                self.assertEqual(True, True)
            except:
                self.assertEqual(False, True)

    def test_undo_redo(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        val = Validation()
        un_serv = UndoService()
        sv = Service(st_repo, dc_repo, gr_repo, val, un_serv)
        sv.add_student('12345', 'Dan')
        sv.add_student('13467', 'Bob')
        sv.undo()
        self.assertEqual(len(st_repo), 1)
        sv.redo()
        self.assertEqual(len(st_repo), 2)
        sv.add_discipline('12345', 'Math')
        sv.add_discipline('34567', 'FP')
        sv.add_student('54321', 'Roger')
        sv.undo()
        sv.undo()
        sv.redo()
        self.assertEqual(len(st_repo) == 2 and len(dc_repo) == 2, True)
        sv.add_student('54321', 'Roger')
        if sv.redo():
            self.assertEqual(False, True)
        else:
            self.assertEqual(True, True)
        sv.add_grade('11111', '12345', '13467', '10')
        sv.add_grade('22222', '12345', '12345', '4')
        sv.add_grade('33333', '12345', '12345', '5')
        sv.add_grade('44444', '34567', '12345', '3')
        sv.remove_student('12345')
        sv.undo()
        self.assertEqual(len(gr_repo), 4)
        sv.redo()
        self.assertEqual(len(gr_repo), 1)
        for i in range(10):
            sv.undo()
        if sv.undo():
            self.assertEqual(False, True)
        else:
            self.assertEqual(True, True)

    def test_test2_init(self):
        st_repo = Repository()
        dc_repo = Repository()
        gr_repo = Repository()
        try:
            test2_init(st_repo, dc_repo, gr_repo)
            self.assertEqual(True, True)
        except:
            self.assertEqual(False, True)





def test_init(student_repo, discipline_repo, grade_repo):
    l = string.ascii_lowercase
    i = 0
    while i < 10:
        student_id = ''.join(str(random.randint(0, 9)) for i in range(5))
        student_name = ''.join(random.choice(l) for i in range(random.randint(3, 15)))
        try:
            student_repo.add(Student(student_id, student_name))
        except ValidationError:
            i -= 1
        i += 1
    i = 0
    while i < 10:
        discipline_id = ''.join(str(random.randint(0, 9)) for i in range(5))
        discipline_name = ''.join(random.choice(l) for i in range(random.randint(3, 20)))
        try:
            discipline_repo.add(Discipline(discipline_id, discipline_name))
        except ValidationError:
            i -= 1
        i += 1
    i = 0
    student_id_list = student_repo.get_id_list()
    discipline_id_list = discipline_repo.get_id_list()
    while i < 10:
        grade_id = ''.join(str(random.randint(0, 9)) for i in range(5))
        student_id = random.choice(student_id_list)
        discipline_id = random.choice(discipline_id_list)
        grade_value = random.randint(1, 10)
        try:
            grade_repo.add(Grade(grade_id, discipline_id, student_id, str(grade_value)))
        except ValidationError:
            i -= 1
        i += 1

def test2_init(student_repo, discipline_repo, grade_repo):
    student_repo.add(Student('11111', 'Dan'))
    student_repo.add(Student('22222', 'Bob'))
    student_repo.add(Student('33333', 'Roger'))
    student_repo.add(Student('44444', 'Andreea'))
    student_repo.add(Student('55555', 'Stefan'))
    student_repo.add(Student('66666', 'Bonnie'))
    student_repo.add(Student('77777', 'Linda'))
    student_repo.add(Student('88888', 'Garret'))
    student_repo.add(Student('99999', 'Leo'))
    student_repo.add(Student('12345', 'Elena'))

    discipline_repo.add(Discipline('11111', 'Math'))
    discipline_repo.add(Discipline('22222', 'FP'))
    discipline_repo.add(Discipline('33333', 'Analysis'))
    discipline_repo.add(Discipline('44444', 'Arithmetics'))
    discipline_repo.add(Discipline('55555', 'Geometry'))
    discipline_repo.add(Discipline('66666', 'CSA'))
    discipline_repo.add(Discipline('77777', 'Logic'))
    discipline_repo.add(Discipline('88888', 'OOP'))
    discipline_repo.add(Discipline('99999', 'Sport'))
    discipline_repo.add(Discipline('12345', 'Math2'))

    grade_repo.add(Grade('11111', '11111', '11111', 8))
    grade_repo.add(Grade('22222', '22222', '22222', 5))
    grade_repo.add(Grade('33333', '33333', '33333', 6))
    grade_repo.add(Grade('44444', '44444', '44444', 9))
    grade_repo.add(Grade('55555', '55555', '55555', 10))
    grade_repo.add(Grade('66666', '66666', '66666', 4))
    grade_repo.add(Grade('77777', '77777', '77777', 3))
    grade_repo.add(Grade('88888', '88888', '88888', 4))
    grade_repo.add(Grade('99999', '99999', '99999', 2))
    grade_repo.add(Grade('12345', '12345', '12345', 7))
    grade_repo.add(Grade('00000', '22222', '11111', 10))
    grade_repo.add(Grade('54321', '33333', '22222', 9))
    grade_repo.add(Grade('98765', '44444', '33333', 6))
    grade_repo.add(Grade('65432', '55555', '44444', 5))
    grade_repo.add(Grade('13579', '66666', '55555', 7))
    grade_repo.add(Grade('97531', '77777', '66666', 3))
    grade_repo.add(Grade('86420', '88888', '77777', 6))
    grade_repo.add(Grade('02468', '99999', '88888', 9))
    grade_repo.add(Grade('63754', '12345', '99999', 10))
    grade_repo.add(Grade('15476', '11111', '12345', 2))



if __name__ == '__main__':
    unittest.main()
