from pymongo import MongoClient


def get_mongo_client():
    return MongoClient(
        'mongodb+srv://kougi:bZLLIGw5cmoT5VbA@cluster0.wbmr7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


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
