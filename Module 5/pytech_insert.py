#Jessica Harman
#Assignment 5.3
#09/03/2022
from pymongo import MongoClient
url = "mongodb+srv://python:Mu3J8Ul3FDuiQJtU@cluster0.ush2cwx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
jane = {
    'student_id': 1007,
    'first_name': 'Jane',
    'last_name': 'Austen'
}
george = {
    'student_id': 1008,
    'first_name': 'George',
    'last_name': 'Elliot'
}
anne = {
    'student_id': 1009,
    'first_name': 'Anne',
    'last_name': 'Bronte'
}
result_jane = db.students.insert_one(jane).inserted_id
result_george = db.students.insert_one(george).inserted_id
result_anne = db.students.insert_one(anne).inserted_id

print('--INSERT STATEMENTS--')
print('Inserted student records Jane Austen into the students collection with document id', result_jane)
print('Inserted student records George Elliot into the students collection with document id', result_george)
print('Inserted student records Anne Bronte into the students collection with document id', result_anne)
print('End of program, press any key to exit...')