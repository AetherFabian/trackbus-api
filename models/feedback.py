from datetime import datetime
import database

class Feedback():
    
    def __init__(self, content, bus_recognizer, comment_date = None):
        self.comment_date = comment_date
        self.content = content
        self.bus_recognizer = bus_recognizer        
    
    def get_feedback(self):
        response = database.db.feedback.find()
        feedbacks = []
        for feed in response:
            del feed['_id']
            feedbacks.append(feed)
        return feedbacks
    
    def post_feedback(self, request):
        request['comment_date'] = datetime.now()
        database.db.feedback.insert_one(request)
        request.pop('_id')
        return request