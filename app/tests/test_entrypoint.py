from __future__ import absolute_import
import pdb
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from os.path import join, dirname
from dotenv import load_dotenv

from app.workers.twitter.twitter_api import TwitterAPI
from app.workers.database_adapter.mongo_adapter import MongoAdapter

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

if __name__=='__main__':
  # pdb.set_trace()
  twitter_api = TwitterAPI()
  twitter_api.get_and_persist_followers(None)