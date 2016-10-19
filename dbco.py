from pymongo import MongoClient
from credentials import database

client = MongoClient(database)

db = client.flavorednews

print(db.system.users.find({}))
articles = db.articles

# articles.remove({});
print(articles.count())
