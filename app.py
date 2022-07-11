from flask import Flask, render_template, request, jsonify, redirect
from flask import Flask, redirect, url_for
from pymongo import MongoClient
import jwt
import datetime
import hashlib
from datetime import datetime, timedelta
import certifi
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.210xc.mongodb.net/?retryWrites=true&w=majority')
SECRET_KEY = 'SPARTA'
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


# Route for handling the login page logic
@app.route('/api/login', methods=['GET', 'POST'])
def login():
    id_receive=request.form['id']
    pw_receive=request.form['pw']
    # password_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # result = db.user.find_one({'id': id_receive, 'pw': password_hash})
    result = db.user.find_one({'id': id_receive, 'pw': pw_receive})

    error = None
    if request.method == 'POST':
        if result is not None:
            payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            return redirect(url_for('/'))
        else :
            error = 'ID, PW가 맞지 않습니다.'
            return render_template('login.html', error=error)