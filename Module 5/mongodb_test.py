#Jessica Harman
#Assignment 5.2
#09/03/2022

from pymongo import MongoClient
url = "mongodb+srv://python:Mu3J8Ul3FDuiQJtU@cluster0.ush2cwx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
try:
    print('--Pytech Collection List--')
    print(db.list_collection_names())
    print()
    print('   End of program. Press any key to Exit...')
except Exception:
    print('Unable to connect to the server.')