from src.repositories.Repository import Repository
from src.entities.Discipline import Discipline


class DisciplineTextRepo(Repository):
    def __init__(self, file_name='disciplines.txt'):
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
            line = item.id + ';' + item.name
            f.write(line)
            f.write('\n')
        f.close()

    def _load(self):
        f = open(self._fn, 'rt')
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split(';')
            super().add(Discipline(line[0], line[1]))