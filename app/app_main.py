from flask import Flask, request, render_template
import redis
from celery import Celery

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

app = Flask(__name__)
app.config.update(
  CELERY_BROKER_URL='redis://localhost:6379',
  CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

@celery.task()
def add_together(a, b):
  return a + b

default_key = '1'
cache = redis.StrictRedis(host='redis', port=6379, db=0)
cache.set(default_key, "one")

@app.route('/', methods=['GET', 'POST'])
def mainpage():

  key = default_key
  if 'key' in request.form:
      key = request.form['key']

  if request.method == 'POST' and request.form['submit'] == 'save':
    cache.set(key, request.form['cache_value'])

  cache_value = None;
  if cache.get(key):
    cache_value = cache.get(key).decode('utf-8')

  return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
  print("Running Flask Server")
  app.run(host='0.0.0.0')