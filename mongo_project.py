import os
import pymongo
import pymongo.errors
if os.path.exists("env.py"):
    import env

MONGO_URL = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "cat"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB; %s" %e)
        
def show_menu():
    print("")
    print("Add a record")
    print("Find a record by name")
    print("Edit a record")
    print("Exit a record")
    print("Exit the menu")
    
    option = input("Enter an option: ")
    return option



    