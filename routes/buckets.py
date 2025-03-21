from flask import Blueprint, request, jsonify, send_file
from google.cloud import storage
import uuid
from utils.tryconnectgcs import getCredentials
import tempfile

buckets_route = Blueprint('Buckets', __name__)

@buckets_route.route('/')
def listBuckets():
    creds, error = getCredentials()
    if error:
        return jsonify({"erro": error}), 400

    try:
        storage_client = storage.Client(credentials=creds)
        buckets = storage_client.list_buckets()
        bucket_names = [bucket.name for bucket in buckets]
        return jsonify({"buckets": bucket_names})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@buckets_route.route('/', methods=['POST'])
def addBucket():
    creds, error = getCredentials()
    if error:
        return jsonify({"erro": error}), 400

    data = request.get_json()
    if not data or 'bucket_name' not in data:
        return jsonify({"erro": "JSON inválido! 'bucket_name' é obrigatório."}), 400

    try:
        storage_client = storage.Client(credentials=creds)
        bucket_name = f"{data['bucket_name']}-{uuid.uuid4().hex[:6]}"
        bucket = storage_client.create_bucket(bucket_name)
        return jsonify({"mensagem": f"Bucket '{bucket.name}' criado com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@buckets_route.route('/<bucket_name>', methods=['DELETE'])
def deleteBucket(bucket_name):
    creds, error = getCredentials()
    if error:
        return jsonify({"erro": error}), 400

    try:
        storage_client = storage.Client(credentials=creds)
        bucket = storage_client.get_bucket(bucket_name)
        bucket.delete()
        return jsonify({"mensagem": f"Bucket '{bucket_name}' deletado com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@buckets_route.route('/<bucket_name>/files')
def listFiles(bucket_name):
    creds, error = getCredentials()
    if error:
        return jsonify({"erro": error}), 400

    try:
        storage_client = storage.Client(credentials=creds)
        bucket = storage_client.get_bucket(bucket_name)

        blobs = list(bucket.list_blobs())
        file_names = [blob.name for blob in blobs]

        return jsonify({"files": file_names})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@buckets_route.route('/<bucket_name>/files/<file_name>')
def shareFile(bucket_name, file_name):
    creds, error = getCredentials()
    if error:
        return jsonify({"erro": error}), 400

    try:
        storage_client = storage.Client(credentials=creds)
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)

        url = blob.generate_signed_url(expiration=3600)

        return jsonify({"file_url": url})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@buckets_route.route('/<bucket_name>/files/<file_name>/download')
def downloadFile(bucket_name, file_name):
    creds, error = getCredentials()
    if error:
        return jsonify({"erro": error}), 400

    try:
        storage_client = storage.Client(credentials=creds)
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)

        # Criar um arquivo temporário para armazenar o download
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        blob.download_to_filename(temp_file.name)

        # Enviar o arquivo como um anexo
        return send_file(temp_file.name, as_attachment=True, download_name=file_name)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500