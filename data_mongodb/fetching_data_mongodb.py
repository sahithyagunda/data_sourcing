import pandas as pd
import csv
from connecting_mongodb import client  # MongoDB connection imported from external file

# Step 1: Connect to the database and collection
db = client['api_data']
collection = db['fake_user_data']

# Step 2: Query all documents from the collection (excluding the '_id' field)
data = collection.find({}, {"_id": 0})

# Step 3: Loop through the documents and print each one
for document in data:
    print(document)
