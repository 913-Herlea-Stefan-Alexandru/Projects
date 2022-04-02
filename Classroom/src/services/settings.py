import configparser
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

class ConfigError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Settings:
    def __init__(self, file_name = "settings.properties"):
        self._cp = configparser.SafeConfigParser()
        self._fn = file_name
        self._cp.read(self._fn)
        self._repo_type = self._cp['Settings']['repository']
        self._students = self._cp['Settings']['students']
        self._disciplines = self._cp['Settings']['disciplines']
        self._grades = self._cp['Settings']['grades']
        self._ui = self._cp['Settings']['ui']

    @property
    def repo(self):
        return self._repo_type

    @property
    def students(self):
        return self._students

    @property
    def disciplines(self):
        return self._disciplines

    @property
    def grades(self):
        return self._grades

    @property
    def ui(self):
        return self._ui