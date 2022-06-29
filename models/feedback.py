from urllib import response
import database

class Feedback():
    
    def get_feedback():
        response = database.db.feedback.find()
        feedbacks = []
        for feed in response:
            del feed['_id']
            feedbacks.append(feed)
        return feedbacks
    
    def post_feedback(request):
        database.db.feedback.insert_one(request)
        return 'Inserted'