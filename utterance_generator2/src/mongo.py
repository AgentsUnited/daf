import pymongo
import os

database = "agents_united2" #os.getenv("MONGODB")
host = "mongodb"

def get_db():
    m = pymongo.MongoClient("mongodb://{}:27017/".format(host))
    return m[database]

def get_all_collections():
    db = get_db()
    return db.collection_names()

def get_column(column_name):
    db = get_db()
    return db[column_name]

def ready():
    m = pymongo.MongoClient("mongodb://{}:27017/".format(host))
    if database not in m.list_database_names():
        return False
    else:
        return True
