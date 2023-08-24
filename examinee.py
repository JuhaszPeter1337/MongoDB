import random
from person import Person
from db import *


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

