#!/usr/bin/python3
from flask import Flask, escape, render_template
app = flask(__name__)


@app.route('/')
def helo():
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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    '''
    /python/<text> route
    '''
    return 'python {}'.format(text.replace('_', ' '))


@app.route('number/<int:n>')
def number_route(n):
    '''
    /number/<n> route
    '''
    return '{} is a number'.format(int(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    '''
    /number_template/<n> route
    '''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
