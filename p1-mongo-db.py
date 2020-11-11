import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db2"]

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]

mycol = mydb["cust"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
