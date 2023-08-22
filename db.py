from pymongo import MongoClient
from person import Person

if __name__ == "__main__":
    try:
        client = MongoClient("mongodb://localhost:27017/")
        
        # Important: In MongoDB, a database is not created until it gets content!
        mydb = client["diary"]
        
        # Important: In MongoDB, a collection is not created until it gets content!
        mycoll = mydb["students"]

        person = Person("John Doe", 18, "High School of Alabama", 12, "A")
    
        # Add new record to collection
        record = {"name": person.name,
                  "age": person.age,
                  "school": person.school,
                  "grade": person.grade,
                  "number": person.number}
        rec = mycoll.insert_one(record)
  
        for rec in mycoll.find():
            print(rec)
    
    except Exception as e:
        print("An error occurred:", e)
