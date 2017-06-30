'''
Created on Jun 29, 2017

@author: chadd
'''
import TBriot_api
import time
from datetime import datetime

if __name__ == '__main__':
    counter = 0
    print('Program starting...')
    print()
    while True:
        time.sleep(300)
        TBriot_api.execute()
        counter += 1
        print('Executed ' + str(counter) + ' times.')
        print('Last api call was on ' + str(datetime.now()))
        print()
        print()
