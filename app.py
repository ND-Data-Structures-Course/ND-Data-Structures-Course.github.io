import requests
import json 
import os
import sys
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# Database URL's - Course Specific

HOME_PAGE_URL = "cardcontent.json"
            
# End of Database URL's 

@app.route('/', methods=['POST','GET'])
def index():
    filename = os.path.join(app.static_folder, 'localStorage', 'cardcontent.json')

    with open(filename) as test_file:
        data = json.load(test_file)

    return render_template("index.html", chapters=data)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/learn/<ID>')
def learn(ID):
    filename = os.path.join(app.static_folder, 'localStorage', 'learnData.json')
    with open(filename) as test_file:
        Data = json.load(test_file)

    return render_template('learn.html',data_array = Data, Id = ID)


@app.route('/contact', methods=['POST','GET'])
def contact():
	return render_template("contact.html") 

'''
@app.route('/practice', methods=['POST','GET'])
def practice_page():
    response = requests.get(PRACTICE_URL)
    data = response.json()
    if request.method == 'GET':
        return render_template("practice.html",chapters=data)
    if request.method == 'POST':
        chapter_id=request.form.get('id')
        chaptertitle = data[int(chapter_id[0])-1].get('Chapters')[int(chapter_id[2])-1].get('Title')
        print(chaptertitle)
        return render_template("practiceguide.html",title=chaptertitle,count=[1,2,3,4,5,6,7,8,9,10])
    pass

@app.route('/visualize', methods=['POST','GET'])
def visualize_page():
	return render_template("visualize.html") '''
