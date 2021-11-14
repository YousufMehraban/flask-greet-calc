from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def addition():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"""{add(a,b)}"""

@app.route('/sub')
def subtraction():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"""{sub(a,b)}"""

@app.route('/mult')
def multiply():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"""{mult(a,b)}"""

@app.route('/div')
def divide():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"""{div(a,b)}"""

ops = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

@app.route('/math/<operation>')
def math_operation(operation):
    operation = ops[operation]
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operation(a,b)}"
