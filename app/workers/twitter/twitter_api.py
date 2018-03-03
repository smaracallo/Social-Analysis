import os
import tweepy

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

  def get_followers(self):
    followers = self.api.followers(1952074310)
    return followers