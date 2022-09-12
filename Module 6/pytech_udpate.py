#Jessica Harman
#Assignment 6.2
#09/10/2022

from pymongo import MongoClient
url = "mongodb+srv://python:Mu3J8Ul3FDuiQJtU@cluster0.ush2cwx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Darcy"}})

# find the updated student document 
jane = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + jane["student_id"] + "\n  First Name: " + jane["first_name"] + "\n  Last Name: " + jane["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
