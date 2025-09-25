from pymongo import MongoClient

# 1 Estabelece conexão com o MongoDB e o database

client = MongoClient("mongodb://root:rootpass@localhost:27017?authSource=admin")
db = client["nobel"]

prizes = db["prizes"]
laureates = db["laureates"]

# 2 - Contar documentos por gênero
print(laureates.count_documents({"gender": "female"}))
print(laureates.count_documents({"gender": "male"}))

# 3 - Contar documentos pelo país que morreu
print(laureates.count_documents({"diedCountry": "France"}))

# 4 - Filtro composto
filter_doc = {"diedCountry": "France", "gender": "female", "bornCity": "Warsaw"}
print(laureates.count_documents(filter_doc))
print(laureates.find_one(filter_doc))

# 5 - Utilizando o operador in
filter_in = laureates.count_documents({"diedCountry": {"$in": ["France", "USA"]}})
print(filter_in)

# 6 - Utilizando o operador ne - not equal
filter_ne = laureates.count_documents({"diedCountry": {"$ne": "USA"}})
print(filter_ne)
