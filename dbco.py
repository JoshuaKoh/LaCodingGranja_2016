from pymongo import MongoClient
client = MongoClient("mongodb://newsmood:hLQp9PBtdRnJGmKI9FegaJJPLI9T3Yl8vGHrwcXzYLt41dUXYZTzsoA27NrH001CxZbgA0Aqjbio4liIVxKkIA==@newsmood.documents.azure.com:10250/?ssl=true")
db = client['admin']
articles = db.articles
