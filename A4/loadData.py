from pymongo import MongoClient

connection = MongoClient("localhost", 27017)
db = connection.test.diniraw7

data = open("data.txt").read().strip().split("\n")
for line in data:
    record = line.strip().split(", ")
    print record
    post = {"ph_no" : int(record[0]), "temp" : int(record[1])}
    db.insert_one(post)