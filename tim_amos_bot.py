#!/usr/bin/env python

import os
import sys
import random
import subprocess
from twython import Twython


ApiKey = ''
ApiSecret = ''
AccessToken = ''
AccessTokenSecret = ''
cred_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         '.auth')
twitter_allowed_char = 260


def get_api_token():
    ''' Obtain Twitter app's API token from file .auth

    Returns list
    '''
    with open(cred_file, 'rb') as f:
        c = f.read()
        t = c.splitlines()
        return t[0:4]


def get_today_str():
    ''' Obtain current date in 'Month_Date' format, e.g., March 3

    Returns str
    '''
    d = subprocess.check_output(["date", "+%B_%d"])
    d_str = d.strip()
    return d_str.decode('utf-8')


def get_tweet_str():
    ''' Obtain the string to tweet. It does sanity checks.

    Returns str
    '''
    lilis = " @91bowie"
    today_str = get_today_str()
    tweet_str = 'Nothing to tweet today. #' + today_str
    
    tim_amos_list = ["teste de ide", "i know nobody understands me like you do", "You know, when I'm with you I'm so much happier", "tim amos liliquinhas"]
    list_size = len(tim_amos_list)
    if list_size == 0:
        return tweet_str

    else:
        i = random.randrange(0, list_size)
        entry_str = tim_amos_list[i]
        tweet_str = entry_str + lilis

    return tweet_str


def do_tweet(str):
    ''' Tweet str to Twitter

    '''
    [ApiKey, ApiSecret, AccessToken, AccessTokenSecret] = get_api_token()
    api = Twython(ApiKey, ApiSecret, AccessToken, AccessTokenSecret)
    api.update_status(status=str)
    print("Tweeted: ", str)


if __name__ == '__main__':
    tweet_str = get_tweet_str()
    print(tweet_str)
    do_tweet(tweet_str)
