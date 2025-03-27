import json
from google.oauth2 import service_account
from flask import Blueprint, request, jsonify, render_template
from google.cloud import storage
import utils.tryconnectgcs

auth_route = Blueprint('Auth', __name__)

@auth_route.route('/')
def teste():
    return render_template('auth.html')

@auth_route.route('/uploadcredentials', methods =['POST'])
def setCredentials():
    credentials = request.get_json()

    if not credentials:
        return jsonify({"erro": "Nenhum JSON enviado"}), 400

    try:
        credential_str = json.dumps(credentials)
        resp = (jsonify({"mensagem":"Credenciais salvas com sucesso!"}))
        resp.set_cookie("cloud_credentials", credential_str, max_age=60*60*24)

        creds = service_account.Credentials.from_service_account_info(credentials)

        storage_client = storage.Client(credentials=creds)
        buckets = list(storage_client.list_buckets())
        return resp
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@auth_route.route('/getCookie', methods =['GET'])
def getCookie():
    cookie = request.cookies.get('cloud_credentials')
    return cookie