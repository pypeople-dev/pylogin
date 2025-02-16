"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pypeople-dev/pygate for more information
"""

from dotenv import load_dotenv
from pymongo import MongoClient, IndexModel, ASCENDING

load_dotenv()
import os

class Database:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_DB_URI"), serverSelectionTimeoutMS=5000, maxPoolSize=50)
        self.db = self.client.get_database()
        self.initialize_collections()
        self.create_indexes()

    def initialize_collections(self):
        collections = ['user-details']
        for collection in collections:
            if collection not in self.db.list_collection_names():
                self.db.create_collection(collection)
                print(f'Created collection: {collection}')

    def create_indexes(self):
        self.db.users.create_indexes([
            IndexModel([("organization", ASCENDING)], unique=True)
        ])

        # TODO: Remove this before merging to master
        if not self.db.users.find_one({"organization": "pypeople.com"}):
            self.db.users.insert_one({
                "server": "https://pypeople-pygate-dev.pypeople.com",
                "organization": "pypeople.com"
            })


database = Database()

database.initialize_collections()
database.create_indexes()

db = database.db