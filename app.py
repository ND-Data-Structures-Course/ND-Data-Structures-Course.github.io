import requests
import json 
import os
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

URL = "URL to database"

@app.route('/', methods=['POST','GET'])
def index():
	return render_template("index.html") #will need to edit later
	''' Sample Code
    response = requests.get(URL)
    data = response.json()
    data = bubble_sort_func(data, 'Maxplayers')

    if request.method == 'GET': # GET request is sent when html wants some information from the python script
        return render_template('index.html', numgames = 0)
    
    if request.method == 'POST': # POST request is sent when the html is sending sdata to the python code for processing
        numplayers=request.form.get('numplayers')
        genre = request.form.get('genre')
        mode = request.form.get('mode')

        dataout = findmatches(data, numplayers, genre, mode)
        length = len(dataout)
 
    return render_template("index.html", numgames = length, games = dataout,numelements = True) '''

def check_valid(data):
	pass #remove this line when you want to actually run the function
	# if information is missing, add default values here
	'''default = {"Title": "Error XXX","Para1":"","Para2":""} #based on the layout we go for
    for attribute in defaults:
        if attribute not in data:
            data[attribute] = defaults[attribute]'''


@app.route('/learn', methods=['POST','GET']) #for learn page
def ast():
	# add return statement here to render template
	pass
	''' Sample Code
    print("Webpage change initiated")
    if request.method == 'GET': # GET request is sent when html wants some information from the python script
        return render_template('ast.html', showast = 0)
    if request.method == 'POST':
        return render_template('ast.html', showast = 1)'''