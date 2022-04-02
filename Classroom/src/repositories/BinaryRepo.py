from src.repositories.Repository import Repository
import pickle

class BinaryRepo(Repository):
    def __init__(self, file_name):
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
        f = open(self._fn, 'wb')
        for item in self._list:
            pickle.dump(item, f)
        f.close()

    def _load(self):
        f = open(self._fn, 'rb')
        while True:
            try:
                super().add(pickle.load(f))
            except EOFError:
                break
        f.close()