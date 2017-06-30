'''
Created on Jun 28, 2017

@author: chadd
'''
import tweepy

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_api(config):
    auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])
    return tweepy.API(auth)

def post(tweet):
# Fill in the values noted in previous step here
    config = { 
    "consumer_key"        : "2Rfj1Ryae4CRMXUmkKDDEFYIm",
    "consumer_secret"     : "a6GpsaqVzEOkJ0CENQADKGpbVMtckhsG3stF9MNfIjcayg0Dkf",
    "access_token"        : "880261980162056194-sFdY2FjUfzz2akOPAWF75xYPjFXLMh8",
    "access_token_secret" : "R5iKxQMMevVUJYF3Rf05iALOHfYBkE4l529XyP2px353A" 
    }

    api = get_api(config)
    status = api.update_status(status=tweet) 
    # Yes, tweet is called 'status' rather confusing
    


# if __name__ == "__main__":
#     post()


