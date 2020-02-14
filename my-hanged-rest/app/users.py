# coding: utf-8
from app import app
import os, json
from flask import request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost') 
db = client['hanged'] # Crear o define db, se crean sin colecciones ni documentos
col = db['users'] # Crear o define colección sin documentos


############
# USUARIOS #
############

# Api para consultar usuarios
@app.route('/users',methods=['GET'])
def getUser():
	data = {} # Creo una data vacía
	data['user'] = [] # Le asigno un valor game
	for doc in col.find({}): # Recorro y agrego valores a data
		idUser = str(doc['_id'])
		data['user'].append({
			'id': idUser,
			'name': doc['name'],
			'email': doc['email'],
			'pass': doc['pass']
		})
	#print(doc)
	#print("Data", doc)
	#return jsonify({"users":data['user'], "message":"User's List"})
	return jsonify(data['user'])

# Api para consultar un usuario por id
@app.route('/users/<string:userId>',methods=['GET'])
def getUserId(userId):
	try:
		data = {} # Creo una data vacía
		data['user'] = [] # Le asigno un valor 
		doc = col.find_one({
			'_id': ObjectId(userId)
		})
		idUser = str(doc['_id'])
		data['user'].append({
			'id': idUser,
			'email': doc['email'],
			'pass': doc['pass']
		})
		#return jsonify({"users":data['user'],"message":"User found"})
		return jsonify(data['user'])
	except:
		return jsonify({"message":"User not found!"})

# Api para crear nuevos usuarios [Login]
@app.route('/users',methods=['POST'])
def addUser():
	try:
		#print(request.json) #Recibe los niveles
		try:
			data = {} # Creo una data vacía
			data['user'] = [] # Le asigno un valor 
			doc = col.find_one({
				'_id': ObjectId(userId)
			})
			#return jsonify({"users":data['user'],"message":"Word found"})
			return jsonify(data['user'])
		except:
			col.insert_one({ # Insertar un documento
				'name': request.json['name'],
				'mail': request.json['mail']
			})
			return jsonify({"message": "User added succesfully!", "user":request.json})
	except:
		return jsonify({"message":"Error added User, validate the fields!"})

# Api para editar un usuario por id
@app.route('/users/<string:userId>',methods=['PUT'])
def editUsers(userId):
	try:
		doc = col.update_one({
		    '_id': ObjectId(userId)
		},{
		    '$set': {
		    	"name":request.json['name'],
				"mail":request.json['mail']
		    }
		})
		return jsonify({"user":request.json,"message": "User Updated!"})
	except:
		return jsonify({"message":"User not found!"})

# Api para eliminar un usuario por id
@app.route('/users/<string:userId>',methods=['DELETE'])
def deleteUser(userId):
	try:
		col.delete_one({
		    '_id': ObjectId(userId)
		})
		return jsonify({"message": "User Deleted!"})
	except (e):
		return jsonify({"message":"User not found!"})