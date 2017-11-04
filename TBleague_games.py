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
    #checks for new games every 5 minutes and tells the user how many times it has been executed and the last execution for 
    #debugging purposes. 
    while True:
        time.sleep(300)
        TBriot_api.execute()
        counter += 1
        print('Executed ' + str(counter) + ' times.')
        print('Last api call was on ' + str(datetime.now()))
        print()
        print()
