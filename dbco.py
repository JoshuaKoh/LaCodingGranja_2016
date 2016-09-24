from pymongo import MongoClient
client = MongoClient("")
db = client['admin']
articles = db.articles