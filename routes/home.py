from flask import Blueprint

home_route = Blueprint('Home', __name__)

@home_route.route('/')
def helloWorld():
    return 'A API Está funcionando'