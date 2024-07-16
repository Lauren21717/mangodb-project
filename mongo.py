import os 
import pymongo
import pymongo.errors
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "cat"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s"  %e)


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]





for doc in documents:
    print(doc)