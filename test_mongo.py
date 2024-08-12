from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.test_database
collection = db.test_collection

# Insert a document
result = collection.insert_one({"name": "test", "value": 123})
print(f"Inserted document with id: {result.inserted_id}")

# Retrieve the document
retrieved_document = collection.find_one({"name": "test"})
print("Retrieved document:", retrieved_document)