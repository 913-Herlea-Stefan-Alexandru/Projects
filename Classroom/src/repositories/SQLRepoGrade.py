from src.repositories.Repository import Repository
from pymongo import MongoClient
from src.entities.Grade import Grade
from pprint import pprint

class SqlRepositoryGr(Repository):
    def __init__(self):
        super().__init__()
        self.client = MongoClient()
        self.db = self.client["classroom"]
        self.grades = self.db["grades"]
        self.load()

    def add(self, item):
        super().add(item)
        student_details = {
            'id': item.id,
            'student_id': item.student_id,
            'discipline_id': item.discipline_id,
            'Value': item.grade_value
        }
        self.grades.insert_one(student_details)

    def remove(self, item):
        super().remove(item)
        self.db.grades.delete_one({'id': item.id})

    def load(self):
        for gr in self.grades.find():
            super().add(Grade(gr['id'], gr['discipline_id'], gr['student_id'], gr['Value']))