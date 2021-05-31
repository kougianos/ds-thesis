from pymongo import MongoClient

client = MongoClient(open('../docs/credentials'))

print(client.list_database_names())

x = client.list_database_names()
testDb = client.get_database('testDb')

col = testDb.get_collection('testCollection')

result = list(col.find())
pass
