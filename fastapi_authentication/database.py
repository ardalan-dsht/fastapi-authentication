import os

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

username = os.environ["MONGO_USER_USERNAME"]
password = os.environ["MONGO_USER_PASSWORD"]
host = os.environ["MONGO_USER_HOST"]
port = os.environ["MONGO_USER_PORT"]
db_name = os.environ["MONGO_USER_DBNAME"]
collection_name = os.environ["MONGO_USER_COLLECTION"]

connection_string = f"mongodb://{username}:{password}@{host}:{port}/"
client = MongoClient(connection_string)
try:
    client.admin.command("ping")
    db_users_collection = client[db_name][collection_name]
    print("Connected to MongoDB successfully!")
except ConnectionFailure as e:
    raise ConnectionFailure(f"Could not connect to the authentication database: {e}")
