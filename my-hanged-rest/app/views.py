# coding: utf-8
from app import app
import os, json
#flask related imports
from flask import render_template, request, jsonify, send_from_directory, send_file, session, redirect, g
#En su momento se utilizó para hacer todas las api de manera local
#from app import apiDB
#Importación mongodb
from pymongo import MongoClient

###########
# NIVELES #
###########

# Api para consultar todos los niveles
client = MongoClient('localhost') 
db = client['hanged'] # Crear o define db, se crean sin colecciones ni documentos
colLeves = db['levels'] # Crear o define colección sin documentos
@app.route('/levels',methods=['GET'])
def getLevels():
	data = {} # Creo una data vacía
	data['levels'] = [] # Le asigno un valor levels
	for doc in colLeves.find({}): # Recorro y agrego valores a data
		data['levels'].append({
		'name': doc['name'],
		'attemptScore': doc['attemptScore'],
		'activate': doc['activate'],
		})
	#   print(doc)
	# print("Data", data)
	return jsonify({"levels":data['levels'], "message":"Level's List"})

# Api para consultar un nivel por id
@app.route('/levels/<int:levelsId>',methods=['GET'])
def getLevelId(levelsId):
	try:
		data = {} # Creo una data vacía
		data['levels'] = [] # Le asigno un valor levels
		docLeves = colLeves.find_one({
			'attemptScore': levelsId
		})
		data['levels'].append({
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
	colLeves = db['levels'] # Crear o define colección sin documentos
	#print(request.json) #Recibe los niveles
	colLeves.insert_one({ # Insertar un documento
	  "name":request.json['name'],
  	  "attemptScore":request.json['attemptScore'],
	  "activate":request.json['activate']
	})
	return jsonify({"message": "Level added succesfully!", "level":request.json})

# Api para editar un nivel por id
@app.route('/levels/<int:levelsId>',methods=['PUT'])
def editLevels(levelsId):
	try:
		data = {} # Creo una data vacía
		data['levels'] = [] # Le asigno un valor levels
		docLeves = colLeves.find_one({
			'attemptScore': levelsId
		})
		data['levels'].append({
			'name': docLeves['name'],
			'attemptScore': docLeves['attemptScore'],
			'activate': docLeves['activate'],
		})
		docLeves = colLeves.update_one({ # Editar todas las colecciones cuyo precio sea igual a 80 y le asigna el precio 90
		    "attemptScore": levelsId
		},{
		    '$set': {
		    	"name":request.json['name'],
				"attemptScore":request.json['attemptScore'],
				"activate":request.json['activate']	
		    }
		})
		return jsonify({"levels":request.json,"message":"Level found"})
	except:
		return jsonify({"message":"Level not found!"})

# Api para eliminar un nivel por id
@app.route('/levels/<int:levelsId>',methods=['DELETE'])
def deleteLevel(levelsId):
	try:
		data = {} # Creo una data vacía
		data['levels'] = [] # Le asigno un valor levels
		docLeves = colLeves.find_one({
			'attemptScore': levelsId
		})
		data['levels'].append({
			'name': docLeves['name'],
			'attemptScore': docLeves['attemptScore'],
			'activate': docLeves['activate'],
		})
		colLeves.delete_one({ # Elimina una colección con el precio igual a 20
		    'attemptScore':levelsId
		})
		return jsonify({"message":"Level deleted!"})
	except:
		return jsonify({"message":"Level not found!"})

############
# PALABRAS #
############

# Api para consultar palabras
@app.route('/words',methods=['GET'])
def getWord():
	return jsonify({"words":apiDB.words, "message":"Word's List"})

# Api para consultar una palabra por id
@app.route('/words/<int:wordsId>',methods=['GET'])
def getWordId(wordsId):
	wordFound = [word for word in apiDB.words if word['id'] == wordsId]
	if (len(wordFound) > 0):	
		return jsonify({"message": "Word Found!", "word":wordFound})
	return jsonify({"message":"Word not found"})

# Api para crear nuevas palabras
@app.route('/words',methods=['POST'])
def addWord():
	#print(request.json) #Recibe las palabras
	newWord = {
		"id":request.json['id'],
		"word":request.json['word'],
		"levelId":request.json['levelId']
	}
	apiDB.words.append(newWord)
	return jsonify({"message": "Word added succesfully!", "word":apiDB.words})

# Api para editar una palabra por id
@app.route('/words/<int:wordsId>',methods=['PUT'])
def editWords(wordsId):
	wordFound = [word for word in apiDB.words if word['id'] == wordsId]
	if (len(wordFound) > 0):
		wordFound[0]['id'] = request.json['id']
		wordFound[0]['word'] = request.json['word']
		wordFound[0]['levelId'] = request.json['levelId']		
		return jsonify({"message": "Word Updated!", "word": wordFound})
	return jsonify({"message":"Word not found"})

# Api para eliminar una palabra por id
@app.route('/words/<int:wordsId>',methods=['DELETE'])
def deleteWord(wordsId):
	wordFound = [word for word in apiDB.words if word['id'] == wordsId]
	if (len(wordFound) > 0):	
		apiDB.words.remove(wordFound[0])	
		return jsonify({"message": "Word Deleted!", "word":apiDB.words})
	return jsonify({"message":"Word not found"})

############
# PARTIDAS #
############
# Api para consultar partidas
@app.route('/game',methods=['GET'])
def getGame():
	return jsonify({"game":apiDB.game, "message":"Game's List"})

# Api para consultar una palabra por id
@app.route('/game/<int:userId>',methods=['GET'])
def getGameId(userId):
	gameFound = [game for game in apiDB.game if game['userId'] == userId]
	if (len(gameFound) > 0):	
		return jsonify({"message": "Game Found!", "game":gameFound})
	return jsonify({"message":"Game not found"})

# Api para crear nuevas partidas
@app.route('/game',methods=['POST'])
def addGame():
	#print(request.json) #Recibe las partidas
	newGame = {
		"userId":request.json['userId'],
		"wordId":request.json['wordId'],
		"letters":request.json['letters'],
		"number-attemps":request.json['number-attemps'],
		"status":request.json['status'],
		"score":request.json['score'],
		"date":request.json['date']
	}
	apiDB.game.append(newGame)
	return jsonify({"message": "Game added succesfully!", "game":apiDB.game})

# Api para editar una partida por id
@app.route('/game/<int:userId>',methods=['PUT'])
def editGame(userId):
	gameFound = [game for game in apiDB.game if game['userId'] == userId]
	if (len(gameFound) > 0):
		gameFound[0]['userId'] = request.json['userId'],
		gameFound[0]['wordId'] = request.json['wordId'],
		gameFound[0]['letters'] = request.json['letters'],
		gameFound[0]['number-attemps'] = request.json['number-attemps'],
		gameFound[0]['status'] = request.json['status'],
		gameFound[0]['score'] = request.json['score'],
		gameFound[0]['date'] = request.json['date']	
		return jsonify({"message": "Game Updated!", "game": gameFound})
	return jsonify({"message":"Game not found"})

# Api para eliminar una partida por id
@app.route('/game/<int:userId>',methods=['DELETE'])
def dateleGame(userId):
	gameFound = [game for game in apiDB.game if game['userId'] == userId]
	if (len(gameFound) > 0):	
		apiDB.game.remove(gameFound[0])	
		return jsonify({"message": "Game Deleted!", "game":apiDB.game})
	return jsonify({"message":"Game not found"})

############
# USUARIOS #
############

# Api para consultar usuarios
@app.route('/users',methods=['GET'])
def getUser():
	return jsonify({"users":apiDB.users, "message":"User's List"})

# Api para consultar un usuario por id
@app.route('/users/<int:userId>',methods=['GET'])
def getUserId(userId):
	userFound = [user for user in apiDB.users if user['id'] == userId]
	if (len(userFound) > 0):	
		return jsonify({"message": "User Found!", "user":userFound})
	return jsonify({"message":"User not found"})

# Api para crear nuevos usuarios
@app.route('/users',methods=['POST'])
def addUser():
	#print(request.json) #Recibe los usuarios
	newUser = {
		"id":request.json['id'],
		"name":request.json['name'],
		"mail":request.json['mail']
	}
	apiDB.users.append(newUser)
	return jsonify({"message": "User added succesfully!", "user":apiDB.users})

# Api para editar un usuario por id
@app.route('/users/<int:userId>',methods=['PUT'])
def editUsers(userId):
	userFound = [user for user in apiDB.users if user['id'] == userId]
	if (len(userFound) > 0):
		userFound[0]['id'] = request.json['id']
		userFound[0]['name'] = request.json['name']
		userFound[0]['mail'] = request.json['mail']		
		return jsonify({"message": "User Updated!", "user": userFound})
	return jsonify({"message":"User not found"})

# Api para eliminar un usuario por id
@app.route('/users/<int:userId>',methods=['DELETE'])
def deleteUser(userId):
	userFound = [user for user in apiDB.users if user['id'] == userId]
	if (len(userFound) > 0):	
		apiDB.users.remove(userFound[0])	
		return jsonify({"message": "User Deleted!", "user":apiDB.users})
	return jsonify({"message":"User not found"})