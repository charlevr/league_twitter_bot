
'''
TAKEN FROM NIKHIL'S BLOG: http://nodotcom.org/python-twitter-tutorial.html
A very helpful and simple tutorial on how to post using tweepy. 
Check out his blog and other such things here: http://nodotcom.org/nikhil-gupta.html
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
    config = { 
    "consumer_key"        : "x",
    "consumer_secret"     : "x",
    "access_token"        : "x",
    "access_token_secret" : "x" 
    }

    api = get_api(config)
    status = api.update_status(status=tweet) 

    




