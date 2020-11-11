import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db2"]

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]


mycol = mydb["cust"]

#mydict = { "name": "hasan", "address": "dik" }

#x = mycol.insert_one(mydict)

myquery = { "address": "dik" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
