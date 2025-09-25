from pymongo import MongoClient

client = MongoClient("mongodb://root:rootpass@localhost:27017?authSource=admin")

my_db = client.dbposts
my_col = my_db.posts

old_value = {"level": "Intermediário"}
new_value = {"$set": {"level": "Iniciante"}}

my_col.update_one(old_value, new_value)

for x in my_col.find():
    print(x)
