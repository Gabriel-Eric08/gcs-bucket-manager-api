from flask import Blueprint, render_template

interface_route = Blueprint('Interface', __name__)

@interface_route.route('/')
def helloWorld():
    return render_template('interfaceSwaggerUI.html')