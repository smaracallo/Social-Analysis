import os
import tweepy
import pdb

class TwitterAPI():

  def __init__(self):
    print('tweet class')
    print(os.environ.get('CONSUMER_KEY'))
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    self.api = tweepy.API(auth)

  def get_followers(self, user_id):
    user_id = 1952074310
    users = self.api.followers(user_id)
    pdb.set_trace()
    #error handling

    # extract provider-follower list from raw data

    # save list of users to db

    # save provider-follower list to db
    return followers