from pymongo import MongoClient

###################
# PARÁMETROS BASE #
###################

client = MongoClient('localhost') 
db = client['hanged'] # Crear o define db, se crean sin colecciones ni documentos
colLeves = db['levels'] # Crear o define colección sin documentos
colUsers = db['users'] # Crear o define colección sin documentos

#Recorrer los documentos
for doc in colLeves.find({}):
  print(doc)

colLeves.insert_one({ # Insertar un documento
  'name': 'Alto',
  'attemptScore': 0,
  'activate': True
})

print ("Cantidad doc levels: ",colLeves.count_documents({})) # Contar los documentos drogas
print ("Cantidad doc users: ",colUsers.count_documents({})) # Contar los documentos usuarios
print ("Nombre de todas las DB: ", client.list_database_names()) # Ver las bases de datos
print ("Nombre de las colecciones en la DB [hanged]: ",db.list_collection_names()) # Ver las colecciones