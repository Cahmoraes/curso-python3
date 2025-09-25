from pymongo import MongoClient

client = MongoClient("mongodb://root:rootpass@localhost:27017/?authSource=admin")
my_db = client.dbposts
mycol = my_db.posts

post1 = {
    "title": "Pandas",
    "category": "Data Analysis",
    "level": "Intermediário",
    "author": {"name": "Rodrigo", "email": "rodrigo@email.com"},
}

result = mycol.insert_one(post1)
print("Documento incluído com sucesso")
