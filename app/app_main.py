from flask import Flask, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
import redis
from celery import Celery
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# see: http://flask.pocoo.org/docs/0.12/patterns/celery/
def make_celery(app):
  celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                  broker=app.config['CELERY_BROKER_URL'])
  celery.conf.update(app.config)
  TaskBase = celery.Task
  class ContextTask(TaskBase):
    abstract = True
    def __call__(self, *args, **kwargs):
      with app.app_context():
        return TaskBase.__call__(self, *args, **kwargs)
  celery.Task = ContextTask
  return celery


# consumer_key = os.environ.get('CONSUMER_KEY')
# consumer_secret = os.environ.get('CONSUMER_SECRET')
# access_token = os.environ.get('ACCESS_TOKEN')
# access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP 
# NOTE this is not the final way that we will be getting data from twitter WIP
app = Flask(__name__)
app.secret_key = "supersekrit"
blueprint = make_twitter_blueprint(
    api_key=os.environ.get('CONSUMER_KEY'),
    api_secret=os.environ.get('CONSUMER_SECRET'),
)
app.config.update(
  CELERY_BROKER_URL='redis://localhost:6379',
  CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

app.register_blueprint(blueprint, url_prefix="/login")

@celery.task()
def add_together(a, b):
  return a + b

default_key = '1'
cache = redis.StrictRedis(host='redis', port=6379, db=0)
cache.set(default_key, "one")

# @app.route('/', methods=['GET', 'POST'])
# def mainpage():

#   key = default_key
#   if 'key' in request.form:
#       key = request.form['key']

#   if request.method == 'POST' and request.form['submit'] == 'save':
#     cache.set(key, request.form['cache_value'])

#   cache_value = None;
#   if cache.get(key):
#     cache_value = cache.get(key).decode('utf-8')

#   return render_template('index.html', key=key, cache_value=cache_value)

@app.route("/")
def index():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    assert resp.ok
    return "You are @{screen_name} on Twitter".format(screen_name=resp.json()["screen_name"])


if __name__ == '__main__':
  print("Running Flask Server")
  app.run(host='0.0.0.0')