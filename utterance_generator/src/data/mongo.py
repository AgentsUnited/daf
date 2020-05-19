import pymongo

class Mongo:
    """ General purpose interface class to streamline mongodb interaction"""

    def __init__(self):
        self.mongodb = pymongo.MongoClient("mongodb://mongodb:27017/")

    def insert(self, db, col, content):
        get_col(db, col).insert_one(content)

    def update_many(self, db, col, filter, query):
        get_col(db, col).update_many(filter, query)

    def get_col(self, db, col):
        db = self.mongodb[db]
        return db[col]
