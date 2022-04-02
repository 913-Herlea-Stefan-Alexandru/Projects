from src.repositories.Repository import Repository
from src.entities.Grade import Grade


class GradeTextRepo(Repository):
    def __init__(self, file_name='grades.txt'):
        super().__init__()
        self._fn = file_name
        self._load()

    def add(self, item):
        super().add(item)
        self._save()

    def remove(self, item):
        super().remove(item)
        self._save()

    def modify(self, item, new_name):
        super().modify(item, new_name)
        self._save()

    def _save(self):
        f = open(self._fn, 'wt')
        for item in self._list:
            line = item.id + ';' + item.discipline_id + ';' + item.student_id + ';' + str(item.grade_value)
            f.write(line)
            f.write('\n')
        f.close()

    def _load(self):
        f = open(self._fn, 'rt')
        lines = f.readlines()
        f.close()

        for line in lines:
            if line != '':
                line = line.split(';')
                super().add(Grade(line[0], line[1], line[2], int(line[3])))