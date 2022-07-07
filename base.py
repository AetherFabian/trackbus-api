from flask import jsonify
import database

class Base():
    
    def check_if_id_exists(self, id):
        if database.db.routes.find_one({'bus_id': id}) or database.db.stops.find_one({'stop_id': id}):
            return True
        else:
            return False
        
    

