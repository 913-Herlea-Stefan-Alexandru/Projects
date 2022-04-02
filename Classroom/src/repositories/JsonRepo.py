import json
from src.repositories.Repository import Repository

class JsonRepo(Repository):
    def __init__(self, origin, file_name):
        super().__init__()
        self._origin = origin
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
        f = open(self._fn, 'w')
        json.dump(self._list, f, default=lambda o: o.__dict__, indent=4)
        f.close()

    def _load(self):
        f = open(self._fn, 'r')
        try:
            read_list = json.load(f)
        except json.decoder.JSONDecodeError:
            return
        for json_dict in read_list:
            json_list = []
            for key in json_dict:
                json_list.append(json_dict[key])
            item = self._origin.from_json(json_list)
            super().add(item)
        f.close()