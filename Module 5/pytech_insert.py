#Jessica Harman
#Assignment 5.3
#09/03/2022
from pymongo import MongoClient
url = "mongodb+srv://python:Mu3J8Ul3FDuiQJtU@cluster0.ush2cwx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

""" three student documents"""

jane = {
    "student_id": "1007",
    "first_name": "Jane",
    "last_name": "Austen",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor",
                    "grade": "A+"
                }
            ]
        }
    ]

}
george = {
    "student_id": "1008",
    "first_name": "George",
    "last_name": "Elliot",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor",
                    "grade": "A-"
                }
            ]
        }
    ]
}
anne = {
    "student_id": "1009",
    "first_name": "Anne",
    "last_name": "Bronte",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                }
            ]
        }
    ]
}
result_jane = db.students.insert_one(jane).inserted_id
result_george = db.students.insert_one(george).inserted_id
result_anne = db.students.insert_one(anne).inserted_id

print('--INSERT STATEMENTS--')
print('Inserted student records Jane Austen into the students collection with document id', result_jane)
print('Inserted student records George Elliot into the students collection with document id', result_george)
print('Inserted student records Anne Bronte into the students collection with document id', result_anne)
print('End of program, press any key to exit...')