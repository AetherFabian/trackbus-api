from datetime import datetime
from dateutil import tz
import database

class Signals():
    
    def __init__(self,  bus_name, stop_id, bus_id, spoted_at=None, status=True):
        self.bus_id = bus_id
        self.bus_name = bus_name
        self.stop_id = stop_id
        self.spoted_at = spoted_at
        self.status = status
    
    def get_bus_by_signals(self, bus_name):
        response_signals = database.db.signals.find({'bus_name': bus_name, 'status': True}, {'stop_id': 1, 'spoted_at': 1})
        response_stops = database.db.stops.find({}, {'stop_id': 1, 'cordinates_x': 1, 'cordinates_y': 1, 'name_stop':1})
        signals = []
        stops = []
        
        for stop in response_stops:
            del stop['_id']
            stops.append(stop)
        for signal in response_signals:
            del signal['_id']
            signals.append(signal)
            
        for x in range(len(stops)):
            for j in reversed(range(len(signals))):
                if signals[j]['stop_id'] == stops[x]['stop_id']:
                    return_signals+=[{'cordinates_x': stops[x]['cordinates_x'], 'cordinates_y': stops[x]['cordinates_y'], 'spoted_at': signals[j]['spoted_at'][17:25], 'name_stop': stops[x]['name_stop']}]
                    break            

        return return_signals
    
    def post_signal(self, request):
        request['spoted_at'] = datetime.now(tz=tz.gettz('America/Chihuahua'))
        return database.db.signals.insert_one(request)