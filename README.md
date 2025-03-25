# 🚀 GCloud Manager API

API para gerenciar buckets e arquivos no Google Cloud Storage. Com esta API, você pode listar buckets, criar e deletar buckets, listar arquivos, fazer download de arquivos, gerar links temporários para compartilhamento e deletar arquivos.

## 🎯 Objetivo

A API tem como objetivo facilitar o gerenciamento de buckets e arquivos no Google Cloud Storage, fornecendo endpoints para operações comuns como listagem, criação, exclusão e compartilhamento de arquivos.

## ☁️ Acessando a API online
Este projeto está hospedado em [meu-domínio.com](https://api-gcs-manager.rj.r.appspot.com).

## Usando a API de forma local.

## 📋 Requisitos

- Python 3.x
- Dependências listadas no arquivo `requirements.txt`
- Uma conta no Google Cloud com permissões para criar e gerenciar buckets.

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone git@github.com:Gabriel-Eric08/gcs-bucket-manager-api.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a API:
   ```bash
   python main.py
   ```

## 🔗 Endpoints

A API oferece os seguintes endpoints:

### `GET /`
📄 Retorna uma interface Swagger UI que documenta todas as rotas, funcionalidades e como usá-las.

### `POST /auth`
🔐 Autentica a API com sua conta do Google Cloud. É necessário enviar um JSON com suas credenciais.

#### 📝 Como obter as credenciais:

1. Acesse sua conta do Google Cloud.
2. Vá para Contas de Serviço.
3. Escolha ou crie uma conta de serviço.
4. Clique em Gerar Chaves para obter o arquivo JSON.

#### 📤 Exemplo de Requisição:
```json
POST /auth
Content-Type: application/json

{
  "type": "service_account",
  "project_id": "seu-projeto",
  "private_key_id": "sua-chave-privada",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "sua-conta-de-servico@seu-projeto.iam.gserviceaccount.com",
  "client_id": "1234567890",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sua-conta-de-servico%40seu-projeto.iam.gserviceaccount.com"
}
```
#### ✅ Resposta:
```json
{
  "message": "Autenticação realizada com sucesso!"
}
```

### `GET /buckets`
📂 Lista todos os buckets do usuário.

#### 📄 Exemplo de Resposta:
```json
{
  "buckets": [
    "seu_bucket",
    "seu_bucket_2"
  ]
}
```

### `POST /buckets`
➕ Cria um novo bucket.

#### 📤 Exemplo de Requisição:
```json
POST /buckets
Content-Type: application/json

{
  "bucket_name": "nome_desejado"
}
```
#### ✅ Resposta:
```json
{
  "message": "Bucket 'nome_desejado' criado com sucesso!"
}
```

### `DELETE /buckets/<bucket_name>`
🗑️ Deleta um bucket existente.

#### 📤 Exemplo de Requisição:
```bash
DELETE /buckets/nome_do_bucket
```
#### ✅ Resposta:
```json
{
  "message": "Bucket 'nome_do_bucket' deletado com sucesso!"
}
```

### `GET /buckets/<bucket_name>/files`
📜 Lista todos os arquivos em um bucket.

#### 📄 Exemplo de Resposta:
```json
{
  "files": [
    "arquivo1.txt",
    "arquivo2.mp4",
    "arquivo3.png"
  ]
}
```

### `GET /<bucket_name>/files/<file_name>`
🔗 Gera um link temporário para compartilhar um arquivo.

#### 📄 Exemplo de Resposta:
```json
{
  "url": "https://storage.googleapis.com/nome_do_bucket/arquivo.txt?generated_token"
}
```

### `DELETE /<bucket_name>/files/<file_name>`
🗑️ Deleta um arquivo de um bucket.

#### 📤 Exemplo de Requisição:
```bash
DELETE /nome_do_bucket/files/arquivo.txt
```
#### ✅ Resposta:
```json
{
  "message": "Arquivo 'arquivo.txt' deletado com sucesso!"
}
```

### `GET /<bucket_name>/files/<file_name>/download`
📥 Faz o download de um arquivo.

#### 📤 Exemplo de Requisição:
```bash
GET /nome_do_bucket/files/arquivo.txt/download
```
#### ✅ Resposta:
O arquivo é baixado diretamente no navegador ou no cliente HTTP.

## 🛠 Exemplos de Uso

### 💻 Exemplo em Python
```python
import requests

# Autenticação
auth_url = "http://localhost:5000/auth"
creds = {...}
response = requests.post(auth_url, json=creds)
print(response.json())

# Listar buckets
buckets_url = "http://localhost:5000/buckets"
response = requests.get(buckets_url)
print(response.json())
```

### 🌐 Exemplo em cURL
```bash
# Autenticação
curl -X POST http://localhost:5000/auth -H "Content-Type: application/json" -d '@creds.json'

# Listar buckets
curl -X GET http://localhost:5000/buckets
```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. 🔀 Faça um fork do repositório.
2. 🛠 Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. 💾 Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. 📤 Faça push para a branch (`git push origin feature/nova-feature`).
<<<<<<< HEAD
5. 🔁 Abra um Pull Request.
=======
5. 🔁 Abra um Pull Request.
>>>>>>> 6c465a053fee6d4beb3cca026c331411eda8668a
