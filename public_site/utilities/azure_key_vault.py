'''
Utility group related to accessing and retreiving items from an Azure Key Vault.
Requires Azure CLI and user authentication
'''
#Import modules
import os
import environ

from pathlib import Path
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


#Initialize environment variables to retreive the name of the Azure Key 
#Vault holding the project's secrets
env = environ.Env()
environ.Env.read_env()

class GetSecret():
    def __init__(
            self,
            p_secret_name
            ):
        self.v_secret_name = p_secret_name
    
    def fxCallSecret(self):    
        v_key_vault_name = 'akv-451-production'
        v_key_vault_uri = f"https://{v_key_vault_name}.vault.azure.net"
        v_credential = DefaultAzureCredential()
        client = SecretClient(vault_url=v_key_vault_uri, credential=v_credential)
        v_secret = client.get_secret(self.v_secret_name)
        return v_secret.value