from pymongo import MongoClient
from person import Person

def connect():
    client = MongoClient("mongodb://localhost:27017/")
        
    # Important: In MongoDB, a database is not created until it gets content!
    mydb = client["diary"]
        
    # Important: In MongoDB, a collection is not created until it gets content!
    my_coll = mydb["students"]

    return my_coll

def add_row_to_db(collection, person):
    record = {"id": person._id,
              "name": person.name,
              "age": person.age,
              "school": person.school,
              "class": person._class,
              "number": person.number,
              "grades": person.grades}
    
    collection.insert_one(record)

def delete_from_db(collection, record):
    collection.delete_one(record)

def update_record(collection, old, new):
    collection.update_one(old, new)

def manipulate_db(my_coll):
        # Add person
        person = Person(1, "John Doe", 27, "Los Angeles High School", 12, "A", [5,2,4,5,1]) 
        add_row_to_db(person)

        # Update record
        my_query = { "name": "John Doe" }
        new_values = { "$set": { "grades": [5,5,5,5] } }
        update_record(my_coll, my_query, new_values)

        # Delete person
        my_query = { "name": "John Doe" }
        delete_from_db(my_coll, my_query)

