import requests
import json 
import os
import sys
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

LEARNPAGE_URL = "https://jsonkeeper.com/b/SM6B"
PRACTICE_URL = ""
DATA_URL=""
@app.route('/', methods=['POST','GET'])
def index():
	return render_template("index.html") #will need to edit later

@app.route('/learn', methods=['POST','GET']) #for learn page
def learn_page():
    response = requests.get(LEARNPAGE_URL)
    data = response.json()
    if request.method == 'GET':
        return render_template("learn.html",chapters=data)
    if request.method == 'POST':
        chapter_id=request.form.get('id')
        chaptertitle = data[int(chapter_id[0])-1].get('Chapters')[int(chapter_id[2])-1].get('Title')
        print(chaptertitle)
        # TODO: get information for topic from database and store the data into a list and pass it into the website
        return render_template("studyguide.html",title=chaptertitle,information=[])
        #make it go to new function generating the new html page
        #return render_template("learn.html",chapters=data) 


@app.route('/contact', methods=['POST','GET']) #for contact page
def contact_page():
	return render_template("contact.html") 


@app.route('/practice', methods=['POST','GET']) #for practice page
def practice_page():
    response = requests.get(PRACTICEPAGE_URL)
    data = response.json()
    if request.method == 'GET':
        return render_template("practice.html",chapters=data)
    if request.method == 'POST':
        chapter_id=request.form.get('id')
        chaptertitle = data[int(chapter_id[0])-1].get('Chapters')[int(chapter_id[2])-1].get('Title')
        print(chaptertitle)
        return render_template("studyguide.html",title=chaptertitle,information=[])
    pass

