import requests
import pymongo
from decouple import config
from azure_cosmodb_for_mongodb import add_user, create_db
from icecream import ic
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv
import os, pathlib


client_id = os.environ.get("AZURECLIENTID")
tenant_id = os.environ.get("AZURETENANTID")
client_secret = os.environ.get("AZURECLIENTSECRET")
account_url = os.environ.get("AZURE_STORAGE_URL")
credentials = ClientSecretCredential(
    tenant_id=tenant_id, client_id=client_id, client_secret=client_secret
)

def upload_blob(local_file_path, blob_name):
    # local_dir = "../input"
    container_name = 'testcontainer'

    # set client to access azure storage container
    blob_service_client = BlobServiceClient(account_url= account_url, credential= credentials)

    # get the container client 
    container_client = blob_service_client.get_container_client(container=container_name)

    with open(local_file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data)


url = "http://localhost:7071/api/http_trigger"
email= "khan@sequenx.com"
password = "1234556"

connection_string = config("PRIMARY_CONNECTION_STRING_MONGO")
client = pymongo.MongoClient(connection_string)

collection = create_db(client)
id = add_user(collection, email, password)


local_file_path = r"D:\2022\Azure-Exploration\input\SBOM_test_SPDX_License.xlsx"
blob_name = pathlib.Path(local_file_path).stem
upload_blob(local_file_path, blob_name)
container_name = 'testcontainer'
result = requests.post(url, params={"id": id, "blobName": blob_name, "containerName":container_name})

ic(result.status_code)
ic(result.text)
ic(result)