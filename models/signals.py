from datetime import datetime
import database

class Signals():
    
    def __init__(self, bus_name, stop_id, spoted_at=None, status=True):
        self.bus_name = bus_name
        self.stop_id = stop_id
        self.spoted_at = spoted_at
        self.status = status
    
    def get_bus_by_signals(self, bus_name):
        response = database.db.signals.find({'bus_name': bus_name})
        signals = []
        for signal in response:
            del signal['_id']
            signals.append(signal)
        return signals
    
    def post_signal(self, request):
        request['spoted_at'] = datetime.now()
        return database.db.signals.insert_one(request)
        