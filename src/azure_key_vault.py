import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, ClientSecretCredential
from decouple import config
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get("AZURECLIENTID")
tenant_id = os.environ.get("AZURETENANTID")
client_secret = os.environ.get("AZURECLIENTSECRET")
vault_url = os.environ.get("AZUREVAULTURL")

# client_id = config("AZURECLIENTID")
# tenant_id = config("AZURETENANTID")
# client_secret = config("AZURECLIENTSECRET")
# vault_url = config("AZUREVAULTURL")

credentials = ClientSecretCredential(
    tenant_id=tenant_id, client_id=client_id, client_secret=client_secret
)

client = SecretClient(vault_url=vault_url, credential=credentials)




# * SETTING

# secretName = "DUMMY2"
# secretValue = "I am going to set a very secret valur on azure"

# print(
#     f"Creating a secret in KV_NAME called '{secretName}' with the value '{secretValue}' ..."
# )

# client.set_secret(secretName, secretValue)

# print(" done.")


# * RETRIVAL

# secretName = "DUMMY2" 

# print(f"Retrieving your secret.")

# retrieved_secret = client.get_secret(secretName)

# print(f"Your secret is '{retrieved_secret.value}'.")


# * DELETION 

secretName = "DUMMY2" 

print(f"Deleting your secret from KV_NAME ...")

poller = client.begin_delete_secret(secretName)
print(poller)
deleted_secret = poller.result()
print(deleted_secret)
print(" done.")
