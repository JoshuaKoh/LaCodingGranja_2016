from pymongo import MongoClient
client = MongoClient("TODO Put Azure key here")
db = client['admin']
stocks = db.stocks