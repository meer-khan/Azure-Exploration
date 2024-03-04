import azure.functions as func
import logging

app = func.FunctionApp()

@app.cosmos_db_trigger(arg_name="azcosmosdb", container_name="users",
                        database_name="TestDB", connection="mongodb2212_DOCUMENTDB",)
def cosmosdb_trigger(azcosmosdb: func.DocumentList):
    logging.info('Python CosmosDB triggered.')
    print(" ***************************** HELLO MY FRIEND ***************************")
    if azcosmosdb:
        logging.info("Document id: %s", azcosmosdb[0])


# import azure.functions as func
# import logging

# app = func.FunctionApp()

# @app.cosmos_db_trigger(arg_name="azcosmosdb", container_name="users",
#                         database_name="TestDB", connection="mongodb2212_DOCUMENTDB")
# def cosmosdb_trigger(azcosmosdb: func.DocumentList):
#     logging.info('Python CosmosDB triggered.')
#     print("MY FRIEND WHO ARE YOU")
#     ic("Hello my friend")
#     ic("record inserted")


# @app.cosmos_db_trigger(
#     connection="mongodb2212_DOCUMENTDB",
#     database_name="TestDB",
#     container_name="users",
#     lease_container_name="leases",
#     create_lease_container_if_not_exists="true",
# )
# def test_function(documents: func.DocumentList) -> str:
#     print(" ***************************** HELLO MY FRIEND ***************************")
#     if documents:
#         logging.info("Document id: %s", documents[0]["id"])
