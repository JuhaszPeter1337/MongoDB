from pymongo import MongoClient
import random
from person import Person

def connect():
    client = MongoClient("mongodb://localhost:27017/")
        
    # Important: In MongoDB, a database is not created until it gets content!
    mydb = client["diary"]
        
    # Important: In MongoDB, a collection is not created until it gets content!
    my_coll = mydb["students"]

    return my_coll

def add_row_to_db(person):
    record = {"id": person._id,
              "name": person.name,
              "age": person.age,
              "school": person.school,
              "class": person._class,
              "number": person.number,
              "grades": person.grades}
    
    my_coll.insert_one(record)

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

if __name__ == "__main__":
    try:
        my_coll = connect()

        print("Class members:")
        for x in my_coll.find():
            print(f'{x["id"]}, {x["name"]}, {x["age"]} years old, {x["school"]}, {x["class"]}/{x["number"]}, Grades: {x["grades"]}')

        length_dict = {}

        my_list = []

        for x in my_coll.find():
            length_dict[x["name"]] = len(x["grades"])
       
        min_value = min(length_dict.values())

        for x in my_coll.find():
            if len(x["grades"]) == min_value:
                my_list.append(x["name"])
                
        print("\nPossible examinee(s):")
        print(*my_list, sep=', ')
        
        if(len(my_list) == 1):
            print(f"\nToday the examinee is {my_list[0]}!")
        else:
            length = len(my_list)
            number = random.randint(0, length-1)
            print(f"\nToday the examinee is {my_list[number]}!")

    except Exception as e:
        print("An error occurred:", e)

