#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    '''
    Hello route
    '''
    return 'hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''
    HBNB route
    '''
    return 'HBNB:'


@app.route('/c/<text>')
def c_text(text):
    '''
    /c/<text> route
    '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python/')
def python_text(text='is cool'):
    '''
    /python/<text> route
    '''
    return 'python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
