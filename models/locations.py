import database

class Locations():
    
    def get_location(bus_name):
        pass
    
    def post_location(request):
        database.db.locations.insert_one(request)
        return ('Location added')