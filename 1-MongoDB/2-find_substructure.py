from pymongo import MongoClient

# 1 Estabelece conexão com o MongoDB e o database

client = MongoClient("mongodb://root:rootpass@localhost:27017?authSource=admin")
db = client["nobel"]

prizes = db["prizes"]
laureates = db["laureates"]

# 2 - Buscando o primeiro documento
walter = laureates.find_one({"firstname": "Walter", "surname": "Kohn"})

print(walter)

# 3 - Pesquisando em uma Substructure
california = laureates.count_documents(
    {"prizes.affiliations.name": "University of California"}
)
print(california)

san_francisco = laureates.count_documents(
    {"prizes.affiliations.city": "San Francisco, CA"}
)
print(san_francisco)

# 4 - Conta documentos que não possua uma informação
no_country = laureates.count_documents({"bornCountry": {"$exists": False}})
print(no_country)

# 5 - Verificando se os laureados possuem prêmio
