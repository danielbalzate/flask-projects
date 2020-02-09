# coding: utf-8
from app import app

import os
#flask related imports
from flask import render_template, request, jsonify, send_from_directory, send_file, session, redirect, g
import flask
from app import apiDB

# NIVELES #
# Api para consultar todos los niveles
@app.route('/levels',methods=['GET'])
def getLevels():
	return jsonify({"levels":apiDB.levels, "message":"Level's List"})

# Api para consultar un nivel por id
@app.route('/levels/<int:levelsId>',methods=['GET'])
def getLevelId(levelsId):
	levelFound = [level for level in apiDB.levels if level['id'] == levelsId]
	if (len(levelFound) > 0):	
		return jsonify({"message": "Level Found!", "level":levelFound})
	return jsonify({"message":"Level not found"})

# Api para crear nuevos niveles
@app.route('/levels',methods=['POST'])
def addLevels():
	#print(request.json) #Recibe los niveles
	newLevel = {
		"id":request.json['id'],
		"name":request.json['name'],
		"attemptScore":request.json['attemptScore'],
		"activate":request.json['activate']
	}
	apiDB.levels.append(newLevel)
	return jsonify({"message": "Level added succesfully!", "level":apiDB.levels})

# Api para editar un nivel por id
@app.route('/levels/<int:levelsId>',methods=['PUT'])
def editLevels(levelsId):
	levelFound = [level for level in apiDB.levels if level['id'] == levelsId]
	if (len(levelFound) > 0):
		levelFound[0]['id'] = request.json['id']
		levelFound[0]['name'] = request.json['name']
		levelFound[0]['attemptScore'] = request.json['attemptScore']
		levelFound[0]['activate'] = request.json['activate']			
		return jsonify({"message": "Level Updated!", "level": levelFound})
	return jsonify({"message":"Level not found"})

# Api para eliminar un nivel por id
@app.route('/levels/<int:levelsId>',methods=['DELETE'])
def deleteLevel(levelsId):
	levelFound = [level for level in apiDB.levels if level['id'] == levelsId]
	if (len(levelFound) > 0):	
		apiDB.levels.remove(levelFound[0])	
		return jsonify({"message": "Level Deleted!", "level":apiDB.levels})
	return jsonify({"message":"Level not found"})

# PALABRAS #
# Api para consultar palabras
@app.route('/words',methods=['GET'])
def getWord():
	return jsonify({"words":apiDB.words, "message":"Word's List"})

# Api para eliminar un nivel por id
@app.route('/words/<int:wordsId>',methods=['GET'])
def getWordId(wordsId):
	wordFound = [word for word in apiDB.words if word['id'] == wordsId]
	if (len(wordFound) > 0):	
		return jsonify({"message": "Word Found!", "word":apiDB.words})
	return jsonify({"message":"Word not found"})

# Api para crear nuevos palabras
@app.route('/words',methods=['POST'])
def addWord():
	#print(request.json) #Recibe los palabras
	newWord = {
		"id":request.json['id'],
		"word":request.json['word'],
		"levelId":request.json['levelId']
	}
	apiDB.words.append(newWord)
	return jsonify({"message": "World added succesfully!", "word":apiDB.words})

# Api para editar un palabra por id
@app.route('/words/<int:wordsId>',methods=['PUT'])
def editWords(wordsId):
	wordFound = [word for word in apiDB.words if word['id'] == wordsId]
	if (len(wordFound) > 0):
		wordFound[0]['id'] = request.json['id']
		wordFound[0]['word'] = request.json['word']
		wordFound[0]['levelId'] = request.json['levelId']		
		return jsonify({"message": "Word Updated!", "word": wordFound})
	return jsonify({"message":"Word not found"})

# Api para eliminar un nivel por id
@app.route('/words/<int:wordsId>',methods=['DELETE'])
def deleteWord(wordsId):
	wordFound = [word for word in apiDB.words if word['id'] == wordsId]
	if (len(wordFound) > 0):	
		apiDB.words.remove(wordFound[0])	
		return jsonify({"message": "Word Deleted!", "word":apiDB.words})
	return jsonify({"message":"Word not found"})