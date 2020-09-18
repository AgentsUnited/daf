import pymongo
import os
import os

host = "mongodb"

if os.getenv("DEMO","False") == "True":
    database = "agents_united_demo"
else:
    database = os.getenv("MONGO_DATABASE", "agents_united2")

def get_db():
    #database = "agents_united" #os.getenv("MONGODB")
    mongo = pymongo.MongoClient("mongodb://{}:27017/".format(host))
    return mongo[database]

def get_all_collections():
    db = get_db()
    return db.collection_names()

def get_column(column_name):
    db = get_db()
    return db[column_name]

def get_record_count(column_name):
    db = get_db()
    return get_column(column_name).count_documents({})

def drop_db():
    """
    Will only work when demo is being used
    """
    if database == "agents_united_demo":
        pymongo.MongoClient("mongodb://{}:27017/".format(host)).drop_database(database)
