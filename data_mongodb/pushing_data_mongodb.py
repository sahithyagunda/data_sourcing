import pandas as pd
import csv
from connecting_mongodb import client  # Assumes MongoDB client is defined in a separate file

# Step 1: Connect to your target database and collection
db = client['api_data']
collection = db['fake_user_data']

# Step 2: Specify the CSV file path
csv_file_path = 'fake_user_data.csv'

# Step 3: Read the CSV file and convert each row to a dictionary
documents = []
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        documents.append(row)

# Step 4: Insert the documents into the MongoDB collection
results = collection.insert_many(documents)

# Step 5: Confirm successful insertion
print(f'Inserted {len(results.inserted_ids)} documents into the collection.')
