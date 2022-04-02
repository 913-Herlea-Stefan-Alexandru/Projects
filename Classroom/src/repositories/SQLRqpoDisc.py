from src.repositories.Repository import Repository
from pymongo import MongoClient
from src.entities.Discipline import Discipline
from pprint import pprint

class SqlRepositoryDisc(Repository):
    def __init__(self):
        super().__init__()
        self.client = MongoClient()
        self.db = self.client["classroom"]
        self.disciplines = self.db["disciplines"]
        self.load()

    def add(self, item):
        super().add(item)
        student_details = {
            'id': item.id,
            'Name': item.name
        }
        self.disciplines.insert_one(student_details)

    def remove(self, item):
        super().remove(item)
        self.db.disciplines.delete_one({'id': item.id})

    def modify(self, item, new_name):
        super().modify(item, new_name)
        self.db.disciplines.update_one(
            {'id': item.id},
            {
                "%set":
                    {
                        'id': item.id,
                        'Name': new_name
                    }
            }
        )

    def load(self):
        for disc in self.disciplines.find():
            super().add(Discipline(disc['id'], disc['Name']))