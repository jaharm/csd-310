#Jessica Harman
#Assignment 5.2
#09/03/2022

from pymongo import MongoClient
url = "mongodb+srv://python:Mu3J8Ul3FDuiQJtU@cluster0.ush2cwx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

MongoDB: insert_one()
doc

jane = {

    "student_id" : "1007"
    "first_name" : "Jane",
    "last_name" : "Austen"

        }

george = {

    "student_id" : "1008",
    "first_name" : "George",
    "last_name" : "Elliot"

}

anne = {

    "student_id" : "1009",
    "first_name" : "Anne",
    "last_name" : "Bronte"
}
 
jane_student_id = students.insert_one(jane).inserted_id
george_student_id = students.insert_one(george).inserted_id
anne_student_id = students.insert_one(anne).inserted_id

docs = db.collection_name.find_one({"student_id"}: "")