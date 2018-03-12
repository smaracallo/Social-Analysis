import os
import tweepy
import pdb

from app.workers.database_adapter.mongo_adapter import MongoAdapter

class TwitterAPI():

  def __init__(self):
    print('tweet class!!')
    print('printing something')
    print(os.environ.get('CONSUMER_KEY'))
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    self.api = tweepy.API(auth)
    self.mongo_adapter = MongoAdapter()

  def get_and_persist_followers(self, user_id):
    if user_id == None:
      user_id = self.mongo_adapter.get_random_follower()
      
    users = self.api.followers(user_id, count=100)
    follower_list_response = self.__save_follower_list(user_id, users)
    
    followers_response = self.__save_followers(users)
    #error handling

    # extract provider-follower list from raw data

    # save list of users to db

    # save provider-follower list to db
    return users

  def __save_followers(self, users):
    db_response = self.mongo_adapter.create_or_update_followers(users)
    return db_response

  def __save_follower_list(self, followee, followers_response):

    follower_dict = { "followee": followee }
    follower_list = []
    for follower in followers_response:
      follower_list += [follower.id]
    follower_dict['followers'] = follower_list
    db_response = self.mongo_adapter.create_or_update_follower_list(follower_dict)
    # pdb.set_trace()
    return db_response