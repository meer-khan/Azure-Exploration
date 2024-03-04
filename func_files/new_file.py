import azure.functions as func
import logging

app = func.FunctionApp()

@app.cosmos_db_trigger(arg_name="azcosmosdb", container_name="users",
                        database_name="TestDB", connection="cosmosdbmongodb2212_DOCUMENTDB",
                        create_lease_container_if_not_exists=True, lease_container_name="leases")  
def cosmosdb_trigger(azcosmosdb: func.DocumentList):
    logging.info('Python CosmosDB triggered.')
