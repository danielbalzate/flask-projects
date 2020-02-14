# coding: utf-8
from app import app
import os, json
from flask import request, jsonify, session, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import bcrypt
import codecs

client = MongoClient('localhost') 
db = client['hanged'] # Crear o define db, se crean sin colecciones ni documentos
users = db['users'] # Crear o define colección sin documentos

@app.route('/')
def index():
    if 'email' in session:
     	return jsonify({"message":"You are logged in as: !" + session['email']})

@app.route('/login', methods=['POST'])
def login():
    login_user = users.find_one({'email' : request.json['email']})
    if login_user:
        if bcrypt.hashpw(request.json['pass'].encode('utf-8'), login_user['pass'].encode('utf-8')) == login_user['pass'].encode('utf-8'):
            session['email'] = request.json['email']
            return jsonify({"message":"Logged!"})
        return jsonify({"message":"Invalid password!"})
    return jsonify({"message":"Invalid email!"})

        


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'email': request.json['email']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.json['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.json['name'], 'email': request.json['email'], 'pass' : hashpass})
            session['email'] = request.json['email']
            return jsonify({"message":"Logged!"})
        return jsonify({"message":"That email already exists!"})
    return jsonify({"message":"Template register [Metodo - GET]!"})