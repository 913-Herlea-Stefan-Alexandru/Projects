from src.repositories.Repository import Repository
from pymongo import MongoClient
from src.entities.Student import Student
from pprint import pprint

class SqlRepositoryStud(Repository):
    def __init__(self):
        super().__init__()
        self.client = MongoClient()
        self.db = self.client["classroom"]
        self.students = self.db["students"]
        self.load()

    def add(self, item):
        super().add(item)
        student_details = {
            'id': item.id,
            'Name': item.name
        }
        self.students.insert_one(student_details)

    def remove(self, item):
        super().remove(item)
        self.db.students.delete_one({'id': item.id})

    def modify(self, item, new_name):
        super().modify(item, new_name)
        self.db.students.update_one(
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
        for stud in self.students.find():
            super().add(Student(stud['id'], stud['Name']))