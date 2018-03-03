from __future__ import absolute_import
from celery import Celery
import os
from os.path import join, dirname
from dotenv import load_dotenv
from .twitter.twitter_api import TwitterAPI

dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
load_dotenv(dotenv_path, verbose=True)
print('celery file')
print(os.environ.get('CONSUMER_KEY'))

app = Celery('workers',broker='amqp://admin:mypass@rabbit:5672',backend='rpc://',include=['workers.tasks'])
twitter_api = TwitterAPI()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
  # Calls test('hello') every 10 seconds.
  sender.add_periodic_task(5.0, test_twitter_api.s('test'), name='twitter api test')

  # Calls test('world') every 30 seconds
  # sender.add_periodic_task(3.0, test.s('world'), expires=10)

  # Executes every Monday morning at 7:30 a.m.
  # sender.add_periodic_task(
  #   crontab(hour=7, minute=30, day_of_week=1),
  #   test.s('Happy Mondays!'),
  # )

@app.task
def test(arg):
  print(arg)

@app.task
def test_twitter_api(test_val):
  # print(test_val)
  print(twitter_api.get_followers())