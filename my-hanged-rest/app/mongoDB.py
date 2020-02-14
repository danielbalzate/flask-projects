from pymongo import MongoClient
from bson.objectid import ObjectId
###################
# PARÁMETROS BASE #
###################

client = MongoClient('localhost') 
db = client['hanged'] # Crear o define db, se crean sin colecciones ni documentos
colLeves = db['levels'] # Crear o define colección sin documentos
colUsers = db['users'] # Crear o define colección sin documentos
colWords = db['words'] # Crear o define colección sin documentos

# Recorrer los documentos
for doc in colUsers.find({}):
  print(doc)

# Recorrer los documentos y muestra las drugs con un precio mayor a 20
# for doc in col.find({
#     'price': {
#         '$gt': 20
#     }
# }):
#   print(doc)


print ("Cantidad doc levels: ",colLeves.count_documents({})) # Contar los documentos drogas
print ("Cantidad doc users: ",colUsers.count_documents({})) # Contar los documentos usuarios
print ("Cantidad doc palabras: ",colWords.count_documents({})) # Contar los documentos palabras
print ("Nombre de todas las DB: ", client.list_database_names()) # Ver las bases de datos
print ("Nombre de las colecciones en la DB [hanged]: ",db.list_collection_names()) # Ver las colecciones    