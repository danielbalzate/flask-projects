# coding: utf-8
from app import app
import os, json
#flask related imports
from flask import render_template, request, jsonify, send_from_directory, send_file, session, redirect, g
#En su momento se utilizó para hacer todas las api de manera local
#from app import apiDB
#Importación mongodb
from pymongo import MongoClient
from bson.objectid import ObjectId


###########
# NIVELES #
###########

# Api para consultar todos los niveles
client = MongoClient('localhost') 
db = client['hanged'] # Crear o define db, se crean sin colecciones ni documentos
colLeves = db['levels'] # Crear o define colección sin documentos
colWords = db['words'] # Crear o define colección sin documentos
colGame = db['game'] # Crear o define colección sin documentos
colUsers = db['users'] # Crear o define colección sin documentos
@app.route('/levels',methods=['GET'])
def getLevels():
	data = {} # Creo una data vacía
	data['levels'] = [] # Le asigno un valor levels
	for doc in colLeves.find({}): # Recorro y agrego valores a data
		idLevel = str(doc['_id'])
		data['levels'].append({
		'id': idLevel,
		'name': doc['name'],
		'attemptScore': doc['attemptScore'],
		'activate': doc['activate'],
		})
	  	# print(doc)
	#print("Data", doc)
	return jsonify({"levels":data['levels'], "message":"Level's List"})

# Api para consultar un nivel por id
@app.route('/levels/<string:levelsId>',methods=['GET'])
def getLevelId(levelsId):
	try:
		data = {} # Creo una data vacía
		data['levels'] = [] # Le asigno un valor 
		docLeves = colLeves.find_one({
			'_id': ObjectId(levelsId)
		})
		idLevel = str(doc['_id'])
		data['levels'].append({
			'id': idLevel,
			'name': docLeves['name'],
			'attemptScore': docLeves['attemptScore'],
			'activate': docLeves['activate'],
		})
		return jsonify({"levels":data['levels'],"message":"Level found"})
	except:
		return jsonify({"message":"Level not found!"})
	

# Api para crear nuevos niveles
@app.route('/levels',methods=['POST'])
def addLevels():
	try:
		colLeves = db['levels'] # Crear o define colección sin documentos
		#print(request.json) #Recibe los niveles
		colLeves.insert_one({ # Insertar un documento
		"name":request.json['name'],
		"attemptScore":request.json['attemptScore'],
		"activate":request.json['activate']
		})
		return jsonify({"message": "Level added succesfully!", "level":request.json})
	except:
		return jsonify({"message":"Error added level, validate the fields!"})
# Api para editar un nivel por id
@app.route('/levels/<string:levelsId>',methods=['PUT'])
def editLevels(levelsId):
	try:
		docLeves = colLeves.update_one({
		    '_id': ObjectId(levelsId)
		},{
		    '$set': {
		    	"name":request.json['name'],
				"attemptScore":request.json['attemptScore'],
				"activate":request.json['activate']	
		    }
		})
		return jsonify({"levels":request.json,"message": "Level Updated!"})
	except:
		return jsonify({"message":"Level not found!"})

# Api para eliminar un nivel por id
@app.route('/levels/<string:levelsId>',methods=['DELETE'])
def deleteLevel(levelsId):
	try:
		colLeves.delete_one({
		    '_id': ObjectId(levelsId)
		})
		return jsonify({"message": "Level Deleted!"})
	except (e):
		return jsonify({"message":"Level not found!"})

############
# PALABRAS #
############

# Api para consultar palabras
@app.route('/words',methods=['GET'])
def getWord():
	data = {} # Creo una data vacía
	data['word'] = [] # Le asigno un valor game
	for doc in colWords.find({}): # Recorro y agrego valores a data
		idWord = str(doc['_id'])
		data['word'].append({
			'id': idWord,
			'word': doc['word'],
			'levelWord': doc['levelWord']
		})
	#print(doc)
	#print("Data", doc)
	return jsonify({"words":data['word'], "message":"Word's List"})

# Api para consultar una palabra por id
@app.route('/words/<string:wordsId>',methods=['GET'])
def getWordId(wordsId):
	try:
		data = {} # Creo una data vacía
		data['word'] = [] # Le asigno un valor 
		docWord = colWords.find_one({
			'_id': ObjectId(wordsId)
		})
		idWord = str(docWord['_id'])
		data['word'].append({
			'id': idWord,
			'word': docWord['word'],
			'levelWord': docWord['levelWord']
		})
		return jsonify({"word":data['word'],"message":"Word found"})
	except:
		return jsonify({"message":"Word not found!"})

# Api para crear nuevas palabras
@app.route('/words',methods=['POST'])
def addWord():
	try:
		colWords = db['words'] # Crear o define colección sin documentos
		#print(request.json) #Recibe los niveles
		colWords.insert_one({ # Insertar un documento
		"word":request.json['word'],
		"levelWord":request.json['levelWord']
		})
		return jsonify({"message": "Word added succesfully!", "word":request.json})
	except:
		return jsonify({"message":"Error added word, validate the fields!"})

# Api para editar una palabra por id
@app.route('/words/<string:wordsId>',methods=['PUT'])
def editWords(wordsId):
	try:
		docWord = colWords.update_one({
		    '_id': ObjectId(wordsId)
		},{
		    '$set': {
		    	"word":request.json['word'],
				"levelWord":request.json['levelWord']
		    }
		})
		return jsonify({"word":request.json,"message": "Word Updated!"})
	except:
		return jsonify({"message":"Word not found!"})

# Api para eliminar una palabra por id
@app.route('/words/<string:wordsId>',methods=['DELETE'])
def deleteWord(wordsId):
	try:
		colWords.delete_one({
		    '_id': ObjectId(wordsId)
		})
		return jsonify({"message": "Word Deleted!"})
	except (e):
		return jsonify({"message":"Word not found!"})

############
# PARTIDAS #
############
# Api para consultar partidas
@app.route('/game',methods=['GET'])
def getGame():
	data = {} # Creo una data vacía
	data['game'] = [] # Le asigno un valor game
	for doc in colGame.find({}): # Recorro y agrego valores a data
		idGame = str(doc['_id'])
		data['game'].append({
			'id': idGame,
			'userId': doc['userId'],
			'wordId': doc['wordId'],
			'letters': doc['letters'],
			'number-attemps': doc['number-attemps'],
			'status': doc['status'],
			'score': doc['score'],
			'date': doc['date']
		})
	#print(doc)
	#print("Data", doc)
	return jsonify({"games":data['game'], "message":"Game's List"})

# Api para consultar una partida por id
@app.route('/game/<string:gameId>',methods=['GET'])
def getGameId(gameId):
	try:
		data = {} # Creo una data vacía
		data['game'] = [] # Le asigno un valor 
		doc = colGame.find_one({
			'_id': ObjectId(gameId)
		})
		idGame = str(doc['_id'])
		data['game'].append({
			'id': idGame,
			'userId': doc['userId'],
			'wordId': doc['wordId'],
			'letters': doc['letters'],
			'number-attemps': doc['number-attemps'],
			'status': doc['status'],
			'score': doc['score'],
			'date': doc['date']
		})
		return jsonify({"games":data['game'],"message":"Game found"})
	except:
		return jsonify({"message":"Game not found!"})

# Api para crear nuevas partidas
@app.route('/game',methods=['POST'])
def addGame():
	try:
		colGame = db['game'] # Crear o define colección sin documentos
		#print(request.json) #Recibe los niveles
		colGame.insert_one({ # Insertar un documento
			'userId': request.json['userId'],
			'wordId': request.json['wordId'],
			'letters': request.json['letters'],
			'number-attemps': request.json['number-attemps'],
			'status': request.json['status'],
			'score': request.json['score'],
			'date': request.json['date']
		})
		return jsonify({"message": "Game added succesfully!", "game":request.json})
	except:
		return jsonify({"message":"Error added Game, validate the fields!"})

# Api para editar una partida por id
@app.route('/game/<string:gameId>',methods=['PUT'])
def editGame(gameId):
	try:
		doc = colGame.update_one({
		    '_id': ObjectId(gameId)
		},{
		    '$set': {
		    	'userId': request.json['userId'],
				'wordId': request.json['wordId'],
				'letters': request.json['letters'],
				'number-attemps': request.json['number-attemps'],
				'status': request.json['status'],
				'score': request.json['score'],
				'date': request.json['date']
		    }
		})
		return jsonify({"game":request.json,"message": "Game Updated!"})
	except:
		return jsonify({"message":"Game not found!"})

# Api para eliminar una partida por id
@app.route('/game/<string:gameId>',methods=['DELETE'])
def dateleGame(gameId):
	try:
		colGame.delete_one({
		    '_id': ObjectId(gameId)
		})
		return jsonify({"message": "Game Deleted!"})
	except (e):
		return jsonify({"message":"Game not found!"})

############
# USUARIOS #
############

# Api para consultar usuarios
@app.route('/users',methods=['GET'])
def getUser():
	data = {} # Creo una data vacía
	data['user'] = [] # Le asigno un valor game
	for doc in colUsers.find({}): # Recorro y agrego valores a data
		idUser = str(doc['_id'])
		data['user'].append({
			'id': idUser,
			'name': doc['name'],
			'mail': doc['mail']
		})
	#print(doc)
	#print("Data", doc)
	return jsonify({"users":data['user'], "message":"User's List"})

# Api para consultar un usuario por id
@app.route('/users/<string:userId>',methods=['GET'])
def getUserId(userId):
	try:
		data = {} # Creo una data vacía
		data['user'] = [] # Le asigno un valor 
		doc = colUsers.find_one({
			'_id': ObjectId(userId)
		})
		idUser = str(doc['_id'])
		data['user'].append({
			'id': idUser,
			'name': doc['name'],
			'mail': doc['mail']
		})
		return jsonify({"users":data['user'],"message":"Word found"})
	except:
		return jsonify({"message":"Word not found!"})

# Api para crear nuevos usuarios
@app.route('/users',methods=['POST'])
def addUser():
	try:
		#print(request.json) #Recibe los niveles
		colUsers.insert_one({ # Insertar un documento
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
		doc = colUsers.update_one({
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
		colUsers.delete_one({
		    '_id': ObjectId(userId)
		})
		return jsonify({"message": "User Deleted!"})
	except (e):
		return jsonify({"message":"User not found!"})