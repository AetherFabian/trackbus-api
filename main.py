from crypt import methods
from operator import methodcaller
from urllib.request import Request
from flask import Flask, request, jsonify
from flask_cors import CORS

from models.routes import Routes

app = Flask(__name__)
CORS(app)

@app.route('/')
def ola():
    return jsonify(message='Ola pa')



@app.route('/routes', methods=['GET','POST'])
def routes():
    if request.method == 'GET':
        return jsonify(Routes.get_route())
    elif request.method == 'POST':
        return Routes.post_route(request.get_json())
    
    

@app.route('/routes/<int:bus_id>', methods=['GET','PUT','DELETE'])
def route():
    if request.method == 'GET':
        return jsonify(message='GET')
    elif request.method == 'PUT':
        return jsonify(message='PUT')
    elif request.method == 'DELETE':
        return jsonify(message='DELETE')
       
@app.route('/signals', methods=['GET','POST'])
def signal():
    if request.method == 'GET':
        return jsonify(message='GET')
    elif request.method == 'POST':
        return jsonify(message='POST')
        
@app.route('/locations', methods=['POST'])
def location():
    return jsonify(message='POST')



@app.route('/locations/<string:bus_name>', methods=['GET'])
def locations():
    return jsonify(message='GET')



@app.route('/feedback', methods=['GET','POST'])
def feedbacks():
    if request.method == 'GET':
        return jsonify(message='GET')
    elif request.method == 'POST':
        return jsonify(message='POST')

if __name__ == '__main__':
    app.run(debug=True)

