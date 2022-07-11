from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.210xc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 저장 - 예시
doc = {'id':'qwer1234','pw':1234}
db.users.insert_one(doc)
#