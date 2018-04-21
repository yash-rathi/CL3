from flask import Flask, request, render_template
from booths import *

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('index.html', product = "")

@app.route('/eval', methods = ['POST', 'GET'])
def multiply():
    p = booths(int(request.form['num1']), int(request.form['num2']))
    p = int(''.join("%d"%x for x in p[:-1]), 2)
    return render_template('index.html', product = p)

if(__name__ == "__main__"):
    app.run()