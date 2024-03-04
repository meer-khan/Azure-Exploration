import os
import sys
import pymongo
from decouple import config
from icecream import ic

def create_db(client):
    try:
        database_name = "TestDB"

        # Create or access the specified database
        existing_db = client[database_name]

        # Insert a document into a collection (this will create the database if it doesn't exist)
        collection_test = existing_db["users"]

        return (
            collection_test
        )
    except Exception as e:
        print(f"Error: {e}")



def add_user(collection, email, password): 
    data = collection.insert_one({"email": email, "password": password})
    return str(data.inserted_id)

    
def find_user(collection, email): 
    data = collection.find_one({"email": email})
    return data




if __name__ == "__main__": 
    connection_string = config("PRIMARY_CONNECTION_STRING_MONGO")
    client = pymongo.MongoClient(connection_string)

        # Get server information
    # for k, v in client.server_info().items():
        # print("Key: {} , Value: {}".format(k, v))
    print(client.server_info())
    # Get server status of admin database
    print("Server status {}".format(client.admin.command("serverStatus")))

    # List databases
    databases = client.list_database_names()
    print("Databases: {}".format(databases))

    DB_NAME = "TestDB"
    COLLCECTION = ""
    if DB_NAME in databases:
        collections = client[DB_NAME].list_collection_names()
        COLLCECTION = collections[0]

    oc_count = client[DB_NAME][COLLCECTION].count_documents({})
    ic(oc_count)

    # * Create database
    # collection = create_db(client)
    # print(collection)

    email = "shahmirkhan519@gmail.com"
    password = "0000000"
    # * Add Record
    
    add_user(client[DB_NAME][COLLCECTION], email, password)


    # *  FIND RECORD
    # result = find_user(client[DB_NAME][COLLCECTION],email )
    # ic(result)


