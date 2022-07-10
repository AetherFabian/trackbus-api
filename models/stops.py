import database

class Stops():
    
    def __init__(self, stop_id, cordinates_x, cordinates_y, name_stop, direction):
        self.stop_id = stop_id
        self.cordinates_x = cordinates_x
        self.cordinates_y = cordinates_y
        self.name_stop = name_stop
        self.direction = direction
        
    def get_stops(self):
        response = database.db.stops.find({})
        stops = []
        for stop in response:
            del stop['_id']
            stops.append(stop)
        return stops
    
    def post_stop(request):
        response = database.db.stops.insert_one(request)
        print(request['stop_id'])
        return (request)
    
    def check_if_id_exists(self, stop_id):
        response = database.db.stops.find_one({'stop_id': stop_id})
        if response is not None:
            return True
        else:
            return False