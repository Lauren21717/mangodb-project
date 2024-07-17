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


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
    try:
        doc = coll.find_one({"first": first.lower()}, {"last": last.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No result found.")
        
    return doc
        


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair colour > ")
    breed = input("Enter breed > ")
    
    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender.lower(),
        "hair_color": hair_color.lower(),
        "breed": breed.lower()
    }
    
    try: 
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")    


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selection option 2")
            # find_record()
        elif option == "3":
            print("You have selection option 3")
            # edit_record()
        elif option == "4":
            print("You have selection option 4")
            #exit_record
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")
        
main_loop()