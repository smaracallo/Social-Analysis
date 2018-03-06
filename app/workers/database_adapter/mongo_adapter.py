from pymongo import MongoClient

class MongoAdapter():

  def __init__(self):
    self.client = MongoClient('mongo', 27017) # change the ip and port to your mongo database's
    self.db = self.client.twitter_db
    self.follower_lists = self.db.followers

  def create_follower_list(self, follower_list):
    # test whether the list of followers already exists

    self.follower_lists.insert(follower_list)
    return followers

  def create_users(self, users):
    pass