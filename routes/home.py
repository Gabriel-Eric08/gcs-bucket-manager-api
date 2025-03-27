from flask import Blueprint, render_template

home_route = Blueprint('Home', __name__)

@home_route.route('/')
def helloWorld():
    return render_template('home.html')