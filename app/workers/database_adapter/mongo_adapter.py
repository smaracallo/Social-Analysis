from pymongo import MongoClient

class MongoAdapter():

  def __init__(self):
    self.client = MongoClient('mongo', 27017) # change the ip and port to your mongo database's
    self.db = client.twitter_db
    self.followers_collection = db.followers

  def create_followers(self, followers):
    self.followers_collection.insert(followers)
    return followers