from pymongo import MongoClient

client = MongoClient("mongodb://root:rootpass@localhost:27017?authSource=admin")

my_db = client.dbposts
my_col = my_db.posts

my_query = {"category": "Backend"}
x = my_col.delete_one(my_query)
print(f"{x.deleted_count} documentos(s) excluído(s)")
