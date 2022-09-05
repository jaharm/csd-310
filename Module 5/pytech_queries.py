#Jessica Harman
#Assignment 5.3
#09/03/2022
from pymongo import MongoClient
url = "mongodb+srv://python:Mu3J8Ul3FDuiQJtU@cluster0.ush2cwx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
stu_collection = db.students


find_all = stu_collection.find({})
print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')
for student_id in find_all:
    print('Studnet ID:',student_id['student_id'],'\nFirst Name:',student_id['first_name'],'\nLast Name:',student_id['last_name'])
    print('\n')
    

print('-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --')
find_one = stu_collection.find_one()
print('\nStudnet ID:',find_one['student_id'],'\nFirst Name:',find_one['first_name'],'\nLast Name:',find_one['last_name'])

print('End of program, press any key to exit...')