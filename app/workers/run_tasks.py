from __future__ import absolute_import
from .tasks import longtime_add
from .celery import app
import time
import numpy as np

if __name__ == '__main__':
  # app.conf.beat_schedule = {
  #   'add-every-30-seconds': {
  #       'task': 'tasks.add',
  #       'schedule': 30.0,
  #       'args': (16, 16)
  #   },
  # }
  print('RUNNING!!')
    # for _ in range(0,10):
    #     result = longtime_add.delay('https://jsonplaceholder.typicode.com/posts/1')
    #     print('Task finished?',result.ready())
    #     print('Task result:',result.result)
    #     time.sleep(1)
    #     print('Task finished"',result.ready())
    #     print('Task result:',result.result)