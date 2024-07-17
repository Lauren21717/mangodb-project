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
    print("4. Delete a record")
    print("5. Exit the menu")
    
    option = input("Enter an option: ")
    return option


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No result found.")
        
    return doc
        

def find_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


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


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for key,value in doc.items():
            if key != "_id":
                update_doc[key] = input(key.capitalize() + " [" + value + "] > ")
                
                if update_doc[key] == "":
                    update_doc[key] = value
        
        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())
        
        print("")
        confirmation = input("Is this document you want to delete?\nY or N > ")
        print("")
        
        if confirmation.lower() == "y":
            try:
                coll.delete_one(doc)
                print("Document deleted!")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")
        
main_loop()