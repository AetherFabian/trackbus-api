from email import message
from flask import Flask, request, jsonify
from flask_cors import CORS

from models.route import Route
from models.routes import Routes

app = Flask(__name__)
CORS(app)

@app.route('/')
def ola():
    return jsonify(message='Ola pa')



@app.route('/routes', methods=['GET','POST', 'DELETE'])
def routes():
    if request.method == 'GET':
        return jsonify(Routes.get_route())
    elif request.method == 'POST':
        new_route = Routes(request.json['bus_id'], request.json['bus_name'], request.json['bus_recognizer'])
        if new_route.check_if_id_exists(new_route.bus_id):
            return jsonify(message='ID already exists')
        return Routes.post_route(new_route.__dict__)
    
    

@app.route('/routes/<int:bus_id>', methods=['GET','PUT','DELETE'])
def route(bus_id):
    if request.method == 'GET':
        get_route = Route(bus_id, None, None)
        return jsonify(get_route.get_route(bus_id))
    elif request.method == 'PUT':
        update_route = Route(request.json['bus_id'], request.json['bus_name'], request.json['bus_recognizer'])
        if update_route.check_if_id_exists(bus_id):
            return jsonify(update_route.put_route(update_route.__dict__))
        else:
            return jsonify(message='This bus does not exist')
    elif request.method == 'DELETE':
        delete_route = Route(bus_id, None, None)
        if delete_route.check_if_id_exists(bus_id):
            body = delete_route.get_route(bus_id)
            return jsonify(delete_route.delete_route(body))
        else:
            return jsonify(message='This bus does not exist')
       
        
@app.route('/stops', methods=['POST'])
def location():
    body = request.get_json()
    return jsonify()


@app.route('/signals', methods=['POST'])
def location():
    body = request.get_json()
    return jsonify()


@app.route('/signals/<string:bus_name>', methods=['GET'])
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


