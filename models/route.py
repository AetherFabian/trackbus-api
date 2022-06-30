from urllib import response
import database
from base import Base

class Route(Base):
    
    def get_route(bus_id):
        response = database.db.routes.find_one({'bus_id': bus_id})
        response.pop('_id')
        print(response, bus_id)
        return response
    
    def put_route(bus_id):
        
        if Base.check_if_id_exists(bus_id):
            response = database.db.routes.find_one_and_update()
            return response
        
            
    def delete_route(bus_id):
        if Base.check_if_id_exists(bus_id):
            response = database.db.routes.find_one_and_delete()
            return response