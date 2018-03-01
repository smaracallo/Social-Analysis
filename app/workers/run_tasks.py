from __future__ import absolute_import
from .tasks import longtime_add
import time
import numpy as np

if __name__ == '__main__':
    for _ in range(0,10):
        result = longtime_add.delay(1,2)
        print('Task finished?',result.ready())
        print('Task result:',result.result)
        time.sleep(1)
        print('Task finished"',result.ready())
        print('Task result:',result.result)