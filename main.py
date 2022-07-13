from flask import Flask, request, jsonify
from flask_cors import CORS

from models.route import Route
from models.routes import Routes
from models.signals import Signals
from models.stops import Stops
from models.feedback import Feedback

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
        new_route = Routes(request.json['bus_id'], request.json['bus_name'], request.json['bus_recognizer'])
        if new_route.check_if_id_exists(new_route.bus_id):
            return jsonify(message='ID already exists')
        return Routes.post_route(new_route.__dict__)
    
    

@app.route('/routes/<string:bus_id>', methods=['GET','PUT','DELETE'])
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
       
        
@app.route('/stops', methods=['GET','POST'])
def stops():
    if request.method == 'GET':
        bus_stops = Stops(None, None, None, None, None)
        return jsonify(bus_stops.get_stops())
    elif request.method == 'POST':
        new_stop = Stops(request.json['stop_id'], request.json['cordinates_x'], request.json['cordinates_y'], request.json['name_stop'], request.json['direction'])
        if new_stop.check_if_id_exists(new_stop.stop_id):
            return jsonify(message='ID already exists')
        return Stops.post_stop(new_stop.__dict__)


@app.route('/signals', methods=['POST'])
def signal():
    new_signal = Signals(request.json['bus_name'], request.json['stop_id'], request.json['bus_id'])
    if new_signal.post_signal(new_signal.__dict__):
        return jsonify(message='Signal added')
    else:
        return jsonify(message='It has an error request')
    

@app.route('/signals/<string:bus_name>', methods=['GET'])
def signals(bus_name):
    get_signals = Signals(None, None, None)
    return jsonify(get_signals.get_bus_by_signals(bus_name))


@app.route('/feedback', methods=['GET','POST'])
def feedbacks():
    if request.method == 'GET':
        get_feed = Feedback(None, None, None)
        return jsonify(get_feed.get_feedback())
    elif request.method == 'POST':
        new_feed = Feedback(request.json['content'], request.json['bus_recognizer'])
        return jsonify(new_feed.post_feedback(new_feed.__dict__))

if __name__ == '__main__':
    app.run(load_dotenv=True, port=8080)