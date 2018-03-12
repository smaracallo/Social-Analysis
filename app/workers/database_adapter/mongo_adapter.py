from pymongo import MongoClient
import pdb

class MongoAdapter():

  def __init__(self, port=27017):
    self.client = MongoClient('mongo', port) # change the ip and port to your mongo database's
    # Uncomment for local mode
    # TODO use an ENV var for this please
    # self.client = MongoClient('localhost', 27018)
    self.db = self.client.twitter_db
    self.follower_lists = self.db.follower_lists
    self.followers = self.db.followers

  def create_or_update_follower_list(self, follower_list):
    # test whether the list of followers already exists
    # retrieved_followers = self.follower_lists
    # pdb.set_trace()
    followee = follower_list['followee']
    search_criteria = {'followee': followee}
    follower_exists = self.follower_lists.find_one(search_criteria) != None
    if follower_exists:
      follower_list_response = self.follower_lists.replace_one(search_criteria, follower_list)
    else:
      follower_list_response = self.follower_lists.insert_one(follower_list)
    return follower_list_response

  def create_users(self, users):
    pass

  def get_random_follower(self):
    random_follower = 1952074310
    random_follower_generator = self.followers.aggregate([ { '$sample': { 'size': 1 } } ])
    if random_follower_generator.alive:
      random_follower = random_follower_generator.next()['id']
    return random_follower

  def create_or_update_followers(self, followers):
    followers_response = []
    for follower in followers:
      # pdb.set_trace()
      follower_json = follower._json
      search_criteria = { "id": follower_json['id'] }
      follower_exists = self.followers.find_one(search_criteria) != None
      if follower_exists:
        followers_response.append(self.followers.replace_one(search_criteria, follower_json))
      else:
        followers_response.append(self.followers.insert_one(follower_json))
    return followers_response