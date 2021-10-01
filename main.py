import flask
from flask import request, jsonify, render_template
from utils import *
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods = ['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('/form.html')      
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        return render_template('data.html',form_data = form_data)

@app.route('/form')
def form():
    return render_template('/form.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form.to_dict()
        print(form_data)
        return get_hashes(form_data['siglas_input'])

app.run()