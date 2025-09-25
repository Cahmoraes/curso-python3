from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://root:rootpass@localhost:27017/?authSource=admin")

my_db = client.dbposts
my_col = my_db.posts

result = my_col.find()

for r in result:
    pprint(r)
