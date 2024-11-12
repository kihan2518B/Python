import pymongo
import pandas as pd

# MongoDB connection setup
MONGO_URI = "mongodb+srv://kp648027:kishan@cluster0.8ebnx.mongodb.net/registrationform?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your MongoDB URI
DATABASE_NAME = "registrationform"  # Replace with your database name
COLLECTION_NAME = "users"  # Replace with your collection name

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Fetch data from MongoDB
data = list(collection.find())

# Check if data is not empty
if data:
    # Convert MongoDB documents to DataFrame
    df = pd.DataFrame(data)

    # Remove MongoDB's default '_id' field if not needed
    if '_id' in df.columns:
        df = df.drop('_id', axis=1)

    # Export DataFrame to Excel
    output_file = "mongodb_data.xlsx"
    df.to_excel(output_file, index=False, engine='openpyxl')

    print(f"Data exported successfully to {output_file}")
else:
    print("No data found in the collection.")

# Close the MongoDB connection
client.close()
