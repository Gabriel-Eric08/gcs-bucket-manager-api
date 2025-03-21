from flask import Flask, Blueprint
from routes.home import home_route
from routes.auth import auth_route
from routes.buckets import buckets_route
from routes.teste import teste_route
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(home_route)
app.register_blueprint(teste_route,url_prefix='/teste' )
app.register_blueprint(auth_route, url_prefix='/auth')
app.register_blueprint(buckets_route, url_prefix='/buckets')

if __name__ == "__main__":
    app.run(debug=True)