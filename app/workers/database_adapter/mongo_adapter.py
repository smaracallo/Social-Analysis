from pymongo import MongoClient
import pdb

class MongoAdapter():

  def __init__(self, port=27017):
    self.client = MongoClient('mongo', port) # change the ip and port to your mongo database's
    # Uncomment for local mode
    # TODO use an ENV var for this please
    # self.client = MongoClient('localhost', 27018)
    self.db = self.client.twitter_db
    self.follower_lists = self.db.followers

  def create_or_update_follower_list(self, followee, follower_list):
    # test whether the list of followers already exists
    # retrieved_followers = self.follower_lists
    followers = self.follower_lists.replace_one(followee, follower_list)
    return followers

  def create_users(self, users):
    pass

  def create_or_update_followers(self, followers):
    pass