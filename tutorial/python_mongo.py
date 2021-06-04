from pymongo import MongoClient


def get_mongo_client():
    return MongoClient(open('../docs/credentials'))


# Useful commands
# Get mongo client
client = get_mongo_client()
# Get database names
dbs = client.list_database_names()
# Get specific database
testDb = client.get_database('testDb')
# Get specific collection
collection = testDb.get_collection('testCollection')
# Find all and return result as list of dicts
result = list(collection.find())
pass