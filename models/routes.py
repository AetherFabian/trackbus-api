from flask import jsonify
import database
from models.route import Route

class Routes(Route):
    
    def __init__(self, bus_id, bus_name, bus_recognizer):
        super().__init__(bus_id, bus_name, bus_recognizer)
    
    def get_route():
        try:
            response = list(database.db.routes.find({}, {'bus_name':1, 'bus_id':1}))
            routes = []
            for route in response:
                del route['_id']
                if len(route) > 1:
                    routes.append(route)
            return routes
        except Exception as e:
            return str(e)
    
    def post_route(request):
        database.db.routes.insert_one(request)
        return jsonify(message='Route added')