from urllib import response

from flask import jsonify
import database

class Routes():
    
    def __init__(self):
        pass
    
    def get_route():
        response = list(database.db.routes.find())
        routes = []
        for route in response:
            del route['_id']
            routes.append(route)
        return routes
    
    def post_route(request):
        database.db.routes.insert_one(request)
        return jsonify(message='Route added')