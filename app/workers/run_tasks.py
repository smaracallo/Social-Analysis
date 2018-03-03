from __future__ import absolute_import
from .tasks import longtime_add
from .celery import app
import time
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv

if __name__ == '__main__':
  # app.conf.beat_schedule = {
  #   'add-every-30-seconds': {
  #       'task': 'tasks.add',
  #       'schedule': 30.0,
  #       'args': (16, 16)
  #   },
  # }
  # dotenv_path = join(dirname(__file__), '.env')
  # # load_dotenv(dotenv_path)

  # # OR, the same with increased verbosity:
  # load_dotenv(dotenv_path, verbose=True)
  # print(os.environ.get('CONSUMER_KEY'))
  print('RUNNING!!')

    # for _ in range(0,10):
    #     result = longtime_add.delay('https://jsonplaceholder.typicode.com/posts/1')
    #     print('Task finished?',result.ready())
    #     print('Task result:',result.result)
    #     time.sleep(1)
    #     print('Task finished"',result.ready())
    #     print('Task result:',result.result)