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
       

conn = mongo_connect(MONGO_URL)
coll = conn[DATABASE][COLLECTION]

 
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Exit a record")
    print("5. Exit the menu")
    
    option = input("Enter an option: ")
    return option


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selection option 1")
        elif option == "2":
            print("You have selection option 2")
        elif option == "3":
            print("You have selection option 3")
        elif option == "4":
            print("You have selection option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")
        
