import azure.functions as func
import logging
# import pymongo

app = func.FunctionApp()

@app.cosmos_db_trigger(arg_name="azcosmosdb", container_name="mongodb2212",
                        database_name="TestDB", connection="mongodb2212_DOCUMENTDB")  
def cosmosdb_trigger(azcosmosdb: func.DocumentList):
    logging.info('Python CosmosDB triggered.')
    print("hello")
