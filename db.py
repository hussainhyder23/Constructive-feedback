
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

mydb=client["feed"]
mycol=mydb["feedbacks"]

key=['100','200','210']
value=['hello','hell','hel']

dictn=dict(zip(key,value))

print(dictn)



x=mycol.insert_many([dictn])


