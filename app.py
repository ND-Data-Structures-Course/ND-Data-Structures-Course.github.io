import requests
import json 
import os
import sys
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

LEARNPAGE_URL = "https://jsonkeeper.com/b/SM6B"
PRACTICE_URL = ""
@app.route('/', methods=['POST','GET'])
def index():
	return render_template("index.html") #will need to edit later

def getData(chap_id):
    # scan through all data and get the required information for the relevant chapter based on ID.
    return [] #should return list of dictionariies of images and paragraphs

@app.route('/learn', methods=['POST','GET']) #for learn page
def learn_page():
    response = requests.get(LEARNPAGE_URL)
    data = response.json()
    if request.method == 'GET':
        return render_template("learn.html",chapters=data)
    if request.method == 'POST':
        chapter_id=request.form.get('id')
        currentchapterdata = getData(chapter_id)
        #make it go to new function generating the new html page
        return render_template("learn.html",chapters=data) 


@app.route('/studyguide', methods=['POST','GET'])
def data_page():
    infoset = [] #make a list of all paras and images as needed
    return render_template("studyguide.html",)


@app.route('/contact', methods=['POST','GET']) #for contact page
def contact_page():
	return render_template("contact.html") 


@app.route('/practice', methods=['POST','GET']) #for practice page
def practice_page():
	return render_template("practice.html")

