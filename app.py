from flask import Flask, render_template, request, jsonify, redirect
from flask import Flask, redirect, url_for
from pymongo import MongoClient
import jwt
import datetime
import hashlib
from datetime import datetime, timedelta
import certifi
import requests


from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.210xc.mongodb.net/?retryWrites=true&w=majority')
SECRET_KEY = 'SPARTA'
db = client.dbsparta

app = Flask(__name__)



@app.route('/detail')
def ADD():
    return render_template("detail.html")

@app.route('/')
def home():
    status_receive = request.args.get("status_give")
    travel_list = list(db.travel.find({},{'_id':False}))
    # num =travel_list['num']
    return render_template('index.html',travel=travel_list,status=status_receive,num=num)


@app.route("/travel", methods=["POST"])
def mars_post():
    travel_list = list(db.travel.find({}, {'_id': False}))
    count =len(travel_list) +1
    image_receive = request.form['image_give']
    region_receive = request.form['region_give']
    content_receive=request.form['content_give']
    
    name=request.form['names_give']
    name_receive = name.split('=')[1]
    print(name_receive)
    doc = {
        'image': image_receive,
        'region': region_receive,
        'content': content_receive,
        'name': name_receive,
        'num':count

    }

    db.travel.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})    

@app.route('/api/delete_word', methods=['POST'])
def delete_word(num):
    # 단어 삭제하기
    travel_receive = request.form['travel_give']
    db.travel.delete_one({"travel":travel_receive})
    return jsonify({'result': 'success', 'msg': '삭제완료!'})
    


###############################################################################################################
# 로그인 페이지                                                                                                #
###############################################################################################################
@app.route('/login')
def login():
    return render_template('login.html')


# 로그인 기능 구현
# id,pw를 클라이언트에게 받아와 pw를 해쉬인코딩을 하여 암호화
# id와 암호화한 pw를 mongoDB 내부에 있는지 확인. 없을시 result=None
# 클라이언트에게 받은 id와 pw가 mongoDB와 일치할 시 jwt-token생성 후 
# 클라이언트에게 토큰 전송
@app.route('/api/login', methods=['POST'])
def user_login():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'id': username_receive, 'pw': password_hash})

    
    if result is not None:
        name = result['name']
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token , 'name':name})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디와 비밀번호가 일치하지 않습니다.'})


    
   


###############################################################################################################
# 회원가입 페이지                                                                                              #
###############################################################################################################
@app.route('/signup')
def signup():
    return render_template('signup.html')

    
# 회원가입 id 중복 확인 기능 구현
# 4. id를 클라이언트에서 받아와 mongoDB의 같은 아이디가 있는지 파악
# 5. 있을 시 클라이언트에게 exist=true, 없을 시 =false 반환
@app.route('/api/user_check', methods=['POST'])
def user_check():
    username_receive = request.form['username_give']
    exist = bool(db.users.find_one({"id": username_receive}))
    return jsonify({'result': 'success', 'exist': exist})        
        


# 회원가입 기능 구현
# 4. 클라이언트에게 받아온 id,pw,nickname,  + pw를 해쉬암호화
# 5. id, 암호화한 pw, nickname을 mongoDB에 저장
# 6. 저장되었단 메세지 클라이언트에게 전송 
@app.route('/signup', methods=['POST'])
def signup_success():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.users.insert_one({'id': id_receive, 'pw': pw_hash, 'name': name_receive})

    return jsonify({'result': 'success'})



        






if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)




