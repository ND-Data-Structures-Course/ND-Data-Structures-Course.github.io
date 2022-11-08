import requests
import json 
import os
import sys
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Database URL's - Course Specific

HOME_PAGE_URL = "https://raw.githubusercontent.com/ND-Data-Structures-Course/ND-Data-Structures-Course.github.io/master/cardcontent.json"
#LEARN_PAGE_URL = "" # add Database for chapters     
# End of Database URL's 

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        response = requests.get(HOME_PAGE_URL)
        data = response.json()
        return render_template("index.html", chapters=data)
    if request.method == 'POST':
        return render_template("index.html",chapters=data) #remove this statement and uncomment to finish flask transition
        '''response = requests.get(LEARN_PAGE_URL)
        data = response.json()
        chapter_id=request.form.get('id')
        chapterData = []
        chaptertitle = data[int(chapter_id[0])-1].get('Chapters')[int(chapter_id[2])-1].get('Title')
        response = requests.get(DATA_URL)
        allData = response.json()
        for info in allData:
            if info.get('unique_id') == chapter_id:
                chapterData = info.get('content')
        return render_template("studyguide.html",title=chaptertitle,information=chapterData)'''
