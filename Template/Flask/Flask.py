from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://Santambrogio:wwwws6Ss@cluster0-shard-00-00.r4fcr.mongodb.net:27017,cluster0-shard-00-01.r4fcr.mongodb.net:27017,cluster0-shard-00-02.r4fcr.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-yc014g-shard-0&authSource=admin&retryWrites=true&w=majority'
mongo = PyMongo(app)
CORS(app)


# -------------------------------------------------------------------------------------------------------------------Prova

@app.route('/')
# Prendere i dati da MongoDB
def prova():
    return "Per prendere tutti dati dentro il dataframe aggiungi url + /df "


@app.route('/df')
# Prendere i dati da MongoDB
def get():
    uss = mongo.db.Sito_hotel.find().limit(10)
    resp = json_util.dumps(uss)
    return Response(resp, mimetype='application/json')

if __name__ == '__main__':
    app.run()