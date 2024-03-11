import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()


# @app.cosmos_db_trigger(arg_name="azcosmosdb", container_name="users",
#                         database_name="TestDB", connection="cosmosdbmongodb2212_DOCUMENTDB",
#                         create_lease_container_if_not_exists=True, lease_container_name="leases")  
# def cosmosdb_trigger(azcosmosdb: func.DocumentList):
#     logging.info('Python CosmosDB triggered.')


@app.cosmos_db_trigger(arg_name="azcosmosdb", container_name="users",
                        database_name="TestDB", connection="mongodb://cosmosdbmongodb2212:4utJytmKHP6zIkVFRhbw7l8i8qGIr2pUBWgcyrrXUI74he8tetsDzxCpAeez1G2Yx2Kz9ewJ0bH9ACDb6HqZbg==@cosmosdbmongodb2212.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdbmongodb2212@",
                        create_lease_container_if_not_exists=True, lease_container_name="leases") 
def COSMOSDBTrigger(azcosmosdb: func.DocumentList):
    logging.info('Python CosmosDB triggered.')
    print("HELLOOO MY FIREND")
