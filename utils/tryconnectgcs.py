import json
from google.oauth2 import service_account
from flask import request
from google.cloud import storage

def getCredentials():
    credentials = request.cookies.get('cloud_credentials')
    if not credentials:
        return None, "Credenciais não encontradas!"
    
    try:
        credentials_dic = json.loads(credentials)
        creds = service_account.Credentials.from_service_account_info(credentials_dic)
        return creds, None
    except Exception as e:
        return None, str(e)