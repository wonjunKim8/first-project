from flask import Flask, render_template, request, jsonify
import re
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.210xc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('detail.html')

@app.route("/travel", methods=["POST"])
def mars_post():
    image_receive = request.form['image_give']
    region_receive = request.form['region_give']
    content_receive=request.form['content_give']

    doc = {
        'image': image_receive,
        'region': region_receive,
        'content': content_receive,

    }

    db.travel.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})





if __name__ == '__main__':
   app.run('0.0.0.0', port=8000, debug=True)