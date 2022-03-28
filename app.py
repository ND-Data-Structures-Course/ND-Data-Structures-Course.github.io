import requests
import json 
import os
import sys
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Database URL's - Course Specific
LEARNPAGE_URL = "https://raw.githubusercontent.com/ND-Data-Structures-Course/ND-Data-Structures-Course.github.io/master/learn.json"
PRACTICE_URL = "https://raw.githubusercontent.com/ND-Data-Structures-Course/ND-Data-Structures-Course.github.io/master/practice.json"
DATA_URL="https://jsonkeeper.com/b/2QJ3" #"https://raw.githubusercontent.com/ND-Data-Structures-Course/ND-Data-Structures-Course.github.io/master/chapterdata.json"
# End of Database URL's 

@app.route('/', methods=['POST','GET'])
def index():
	return render_template("index.html")


@app.route('/learn', methods=['POST','GET'])
def learn_page():
    response = requests.get(LEARNPAGE_URL)
    data = response.json()
    if request.method == 'GET':
        return render_template("learn.html",chapters=data)
    if request.method == 'POST':
        chapter_id=request.form.get('id')
        chapterData = []
        chaptertitle = data[int(chapter_id[0])-1].get('Chapters')[int(chapter_id[2])-1].get('Title')
        response = requests.get(DATA_URL)
        allData = response.json()
        for info in allData:
            if info.get('unique_id') == chapter_id:
                chapterData = info.get('content')
        print(chapterData)
        return render_template("studyguide.html",title=chaptertitle,information=chapterData)


@app.route('/contact', methods=['POST','GET'])
def contact_page():
	return render_template("contact.html") 


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
        return render_template("studyguide.html",title=chaptertitle,information=[])
    pass

