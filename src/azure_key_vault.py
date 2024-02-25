import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, ClientSecretCredential
from decouple import config
keyVaultName = "KV_NAME"
KVUri = f"https://KV_NAME.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = "SECRET_NAME"
secretValue = "SECRET_VALUE"

print(f"Creating a secret in KV_NAME called '{secretName}' with the value '{secretValue}' ...")

client.set_secret(secretName, secretValue)

print(" done.")

print(f"Retrieving your secret from KV_NAME.")

retrieved_secret = client.get_secret(secretName)

print(f"Your secret is '{retrieved_secret.value}'.")
print(f"Deleting your secret from KV_NAME ...")

poller = client.begin_delete_secret(secretName)
deleted_secret = poller.result()

print(" done.")
