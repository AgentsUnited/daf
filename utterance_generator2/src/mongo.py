import pymongo
import os

database = "agents_united" #os.getenv("MONGODB")
host = "mongodb"

def get_db():
    database = "agents_united" #os.getenv("MONGODB")
    mongo = pymongo.MongoClient("mongodb://{}:27017/".format(host))
    return mongo[database]

def get_all_collections():
    db = get_db()
    return db.collection_names()

def get_column(column_name):
    db = get_db()
    return db[column_name]
