from src.services.settings import Settings, ConfigError
from src.console.UI import MenuUI
from src.console.GUI import GUI
from src.tests.PyUnit import test2_init
from src.entities.Student import Student
from src.entities.Discipline import Discipline
from src.entities.Grade import Grade
from src.services.services import Service
from src.validators.validator import Validation
from src.repositories.Repository import Repository
from src.repositories.StudentTextRepo import StudentTextRepo
from src.repositories.DisciplineTextRepo import DisciplineTextRepo
from src.repositories.GradeTextRepo import GradeTextRepo
from src.repositories.BinaryRepo import BinaryRepo
from src.repositories.JsonRepo import JsonRepo
from src.services.undoService import UndoService
from src.repositories.SQLRepoStud import SqlRepositoryStud
from src.repositories.SQLRqpoDisc import SqlRepositoryDisc
from src.repositories.SQLRepoGrade import SqlRepositoryGr

if __name__ == '__main__':
    settings = Settings()
    obj = Student
    try:
        if settings.repo == 'inmemory':
            stud_repo = Repository()
            disc_repo = Repository()
            grade_repo = Repository()
            test2_init(stud_repo, disc_repo, grade_repo)
        elif settings.repo == 'textfiles':
            if not (settings.students[-4:] == settings.disciplines[-4:] == settings.grades[-4:] == 'txt"'):
                raise ConfigError('Wrong file types')
            f = open(settings.students.strip('"'), 'a')
            f.close()
            stud_repo = StudentTextRepo(settings.students.strip('"'))
            f = open(settings.disciplines.strip('"'), 'a')
            f.close()
            disc_repo = DisciplineTextRepo(settings.disciplines.strip('"'))
            f = open(settings.grades.strip('"'), 'a')
            f.close()
            grade_repo = GradeTextRepo(settings.grades.strip('"'))
        elif settings.repo == 'binaryfiles':
            if not (settings.students[-4:] == settings.disciplines[-4:] == settings.grades[-4:] == 'bin"'):
                raise ConfigError('Wrong file types')
            f = open(settings.students.strip('"'), 'a')
            f.close()
            stud_repo = BinaryRepo(settings.students.strip('"'))
            f = open(settings.disciplines.strip('"'), 'a')
            f.close()
            disc_repo = BinaryRepo(settings.disciplines.strip('"'))
            f = open(settings.grades.strip('"'), 'a')
            f.close()
            grade_repo = BinaryRepo(settings.grades.strip('"'))
        elif settings.repo == 'jsonfiles':
            if not (settings.students[-5:] == settings.disciplines[-5:] == settings.grades[-5:] == 'json"'):
                raise ConfigError('Wrong file types')
            f = open(settings.students.strip('"'), 'a')
            f.close()
            stud_repo = JsonRepo(Student, settings.students.strip('"'))
            f = open(settings.disciplines.strip('"'), 'a')
            f.close()
            disc_repo = JsonRepo(Discipline, settings.disciplines.strip('"'))
            f = open(settings.grades.strip('"'), 'a')
            f.close()
            grade_repo = JsonRepo(Grade, settings.grades.strip('"'))
        elif settings.repo == 'sql':
            stud_repo = SqlRepositoryStud()
            disc_repo = SqlRepositoryDisc()
            grade_repo = SqlRepositoryGr()
        else:
            raise ConfigError('Wrong settings inside the settings file\nUnknown repo type')
        sv = Service(stud_repo, disc_repo, grade_repo, Validation(), UndoService())
        ui_type = settings.ui
        if settings.ui == '"GUI"':
            ui = GUI(sv)
        elif settings.ui == '"Menu"':
            ui = MenuUI(sv)
        else:
            raise ConfigError('Wrong settings inside the settings file\nUnknown ui type')
        ui.start()
    except ConfigError as ce:
        print(str(ce))