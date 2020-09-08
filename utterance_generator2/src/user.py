import mongo

def get_user(username):
    col = mongo.get_column("users")
    result = col.find_one({"username": username})

    if result is not None:
        return dict(result)
    else:
        return None
