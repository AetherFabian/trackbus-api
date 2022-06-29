import database

class Route():
    
    def get_route(bus_id):
        response = database.db.routes.find_one(bus_id)
        return response
    
    def put_route():
        pass
    
    def delete_route():
        pass