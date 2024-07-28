#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    '''
    Hello route
    '''
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    '''
    HBNB route
    '''
    route 'HBNB:'

@app.route('/c/<text>')
def c_text(text):
    '''
    /c/<text> route
    '''
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
   app.run()
   app.url_map.strict_slashes = False
