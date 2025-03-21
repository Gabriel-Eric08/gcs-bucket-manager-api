from flask import Blueprint, render_template

teste_route = Blueprint('Teste', __name__)

@teste_route.route('/')
def helloWorld():
    cliente = "ASDADS"
    return render_template('index.html', cliente = cliente)