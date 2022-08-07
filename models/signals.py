from datetime import datetime
from re import sub
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
        estimated_times = []
        return_signals = []
        estimate = 0
        
        for stop in response_stops:
            del stop['_id']
            stops.append(stop)
        for signal in response_signals:
            del signal['_id']
            signals.append(signal)
            
        for i in range(len(stops)):
            data = []
            data_sum = 0
            for h in range(len(signals)):
                if stops[i]['stop_id'] == signals[h]['stop_id']:
                    #transformar fechas a horas
                    data.append(signals[h]['spoted_at'])
            # 
            data_sum = max(data) - min(data)
            estimated_times.append(data_sum)
            
        for x in range(len(stops)):
            for j in reversed(range(len(signals))):
                if signals[j]['stop_id'] == stops[x]['stop_id']:
                    return_signals+=[{'cordinates_x': stops[x]['cordinates_x'], 'cordinates_y': stops[x]['cordinates_y'], 'spoted_at': signals[j]['spoted_at'], 'name_stop': stops[x]['name_stop'], 'estimated_time': estimated_times[estimate]}]
                    estimate +=1
                    break            

        return return_signals
    
    def post_signal(self, request):
        request['spoted_at'] = datetime.now()
        return database.db.signals.insert_one(request)
        