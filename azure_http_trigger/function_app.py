import azure.functions as func
import logging
import azure_cosmodb_for_mongodb
import pymongo , os
from bson import ObjectId
from decouple import config
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv
import pandas as pd
import io, tempfile

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger", methods=[func.HttpMethod.GET, func.HttpMethod.POST])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    _id = req.params.get('id')
    container_name = req.params.get('containerName')
    blob_name = req.params.get('blobName')
    print("ID IS: ")
    print(_id)
    # id = req.get_json("id")
    client = get_client()
    collection = create_db(client)
    user = find_user_by_id(collection , _id)
    get_blob_data(blob_name=blob_name, container_name=container_name)
    return func.HttpResponse(f"Hello, {user}. This HTTP triggered function executed successfully.")


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


def get_client():
    connection_string = "mongodb://mongodb2212:7X6r860Iu2V9KGDxP5r5GZSD8KVAsI4CZC2D9tUQPMcgazLZWXBWcylZoeQMxKmZ9rJXsIepSFyYACDbXxfu3Q==@mongodb2212.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mongodb2212@"
    client = pymongo.MongoClient(connection_string)
    return client

def find_user_by_id(collection, id): 
    data = collection.find_one({"_id": ObjectId(id)})
    return data




load_dotenv()

client_id = os.environ.get("AZURECLIENTID")
tenant_id = os.environ.get("AZURETENANTID")
client_secret = os.environ.get("AZURECLIENTSECRET")
account_url = os.environ.get("AZURE_STORAGE_URL")


credentials = ClientSecretCredential(
    tenant_id=tenant_id, client_id=client_id, client_secret=client_secret
)




def get_blob_data(container_name, blob_name):
    
    # container_name = 'testcontainer'
    # blob_name = 'sample3.txt'

    # set client to access azure storage container
    blob_service_client = BlobServiceClient(account_url= account_url, credential= credentials)

    # get the container client 
    container_client = blob_service_client.get_container_client(container=container_name)

    # download blob data 
    blob_client = container_client.get_blob_client(blob= blob_name)

    blob_data = blob_client.download_blob()
    content = blob_data.readall()

    # Read content using Pandas
    # df = pd.read_csv(io.BytesIO(content))  # For CSV file
    df = pd.read_excel(io.BytesIO(content))  # For XLSX file

    print(df)

    write_csv_file(df)
    

def write_csv_file(data_frame): 
    # Write DataFrame to a temporary CSV file
    temp_csv_path = os.path.join(tempfile.gettempdir(), 'temp_file.csv')
    data_frame.to_csv(temp_csv_path, index=False)

    # Perform processing on the CSV file (e.g., read it again)
    processed_df = pd.read_csv(temp_csv_path)

    # Delete the temporary CSV file
    os.remove(temp_csv_path)

    # Alternatively, write DataFrame to a temporary XLSX file
    temp_xlsx_path = os.path.join(tempfile.gettempdir(), 'temp_file.xlsx')
    data_frame.to_excel(temp_xlsx_path, index=False)

    # Perform processing on the XLSX file (e.g., read it again)
    processed_df_xlsx = pd.read_excel(temp_xlsx_path)

    # Delete the temporary XLSX file
    os.remove(temp_xlsx_path)