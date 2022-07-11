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

client = MongoClient('mongodb+srv://test:sparta@cluster0.7nr2yln.mongodb.net/?retryWrites=true&w=majority')
SECRET_KEY = 'SPARTA'
db = client.dbsparta


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)