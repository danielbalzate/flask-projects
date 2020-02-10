from pymongo import MongoClient

#client = MongoClient('localhost', port=27017, user='unser',password:'password') # Forma específica de conectarse

###################
# PARÁMETROS BASE #
###################

client = MongoClient('localhost') 
db = client['test'] # Crear nueva db, se crean sin colecciones ni documentos
col = db['drugs'] # Nueva colección sin documentos
colUsers = db['users'] # Nueva colección sin documentos

#############
# CONSULTAR #
#############

# Recorrer los documentos
# for doc in col.find({}):
#   print(doc)

# Recorrer los documentos y muestra las drugs con un precio mayor a 20
# for doc in col.find({
#     'price': {
#         '$gt': 20
#     }
# }):
#   print(doc)

# Devuelve sólo un documento cuyo precio sea igual a 80
# doc = col.find_one({
#     'price': 80
# })
# print(doc)

#############
# INSERTAR #
#############

# col.insert_one({ # Insertar un documento
#   'price': 20,
#   'name': 'cocaine',
#   'intereses': ['Musica', 'Drugs']
# })

# col.insert_many([ # Insertar varios documentos de drogas
#   {
#     'price': 20,
#     'name': 'cocaine',
#     'intereses': ['Music', 'Drugs']
#   },
#   {
#     'price': 50,
#     'name': 'weed',
#     'intereses': ['Weed', 'Sex']
#   },
#   {
#     'price': 80,
#     'name': 'heroine',
#     'intereses': ['Super Man', 'Drugs']
#   }
# ])

# colUsers.insert_many([ # Insertar varios documentos de usuarios
#   {
#     'price': 20,
#     'name': 'Daniel',
#     'intereses': ['Music', 'Drugs']
#   },
#   {
#     'price': 50,
#     'name': 'Romero',
#     'intereses': ['Weed', 'Sex']
#   },
#   {
#     'price': 80,
#     'name': 'Rosario',
#     'intereses': ['Super Man', 'Drugs']
#   }
# ])

############
# EDITAR #
############

# col.update_many({ # Editar todas las colecciones cuyo precio sea igual a 80 y le asigna el precio 90
#     'price': 80
# },{
#     '$set': {
#         'price':90
#     }
# })

############
# ELIMINAR #
############

# col.delete_one({ # Elimina una colección con el precio igual a 20
#     'price':20
# })

# col.delete_many({ # Elimina todas las  colección con el precio igual a 20
#     'price':20
# })

########################
# ELIMINAR COLECCIONES #
########################

#db.drop_collection('drugs')

###############
# ELIMINAR DB #
###############

#client.drop_database('test')

######################
# CERRAR SESIÓN MONGO#
######################

#client.close()

print ("Cantidad doc drugs: ",col.count_documents({})) # Contar los documentos drogas
print ("Cantidad doc users: ",colUsers.count_documents({})) # Contar los documentos usuarios
print ("Nombre de todas las DB: ", client.list_database_names()) # Ver las bases de datos
print ("Nombre de las colecciones en la DB [test]: ",db.list_collection_names()) # Ver las colecciones