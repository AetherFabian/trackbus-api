import database
class Route():
    
    def __init__(self, bus_id, bus_name, bus_recognizer):
        self.bus_id = bus_id
        self.bus_name = bus_name
        self.bus_recognizer = bus_recognizer
        
    
    def get_route(self, bus_id):
        response = database.db.routes.find_one({'bus_id': bus_id})
        if response is not None:
            response.pop('_id')
            return response
        else:
            return {'message': 'ID does not exist'}
    
    def put_route(self, route):
        database.db.routes.update_one({'bus_id': route['bus_id']}, {'$set': route})
        return route
        
    def delete_route(self, route):
        database.db.routes.delete_one({'bus_id': route['bus_id']})
        return {{'message':'Route deleted'},{route}}
    
    def check_if_id_exists(self, bus_id):
        response = database.db.routes.find_one({'bus_id': bus_id})
        if response is not None:
            return True
        else:
            return False