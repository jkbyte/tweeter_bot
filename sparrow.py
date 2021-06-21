#!/usr/bin/env python3

import random
from twython import Twython
from ssm_secrets import get_secret

# Create the Twython Twitter Client using the credentials 

twitter = Twython(
    get_secret("CONSUMER_KEY"),
    get_secret("CONSUMER_SECRET"),
    get_secret("ACCESS_TOKEN_KEY"),
    get_secret("ACCESS_TOKEN_SECRET")
)

#Sample random tweets
potential_tweets = [
    'This is my first tweet with Sparrow by @jpbot17',
    'Wow! Isn\'t Sparrow by @jpbot17 the coolest',
    'Jeez! Everyone should learn about AWS lambda'
]

def send_tweet(tweet_text):
    """Sends a tweet to Twitter"""
    twitter.update_status(status=tweet_text)

def handler(event,context):
    """Sends random tweet from list of potential tweets list"""
    send_tweet(random.choice(potential_tweets)) 

def follow_someone(screen_name):
    """To follow someone on twitter"""
    twitter.create_friendship(screen_name=screen_name)

def follow_jpbot():
    follow_someone("fmc_sea")

def like_tweet(tweet_id):
    """To like someone on twitter"""
    twitter.create_favorite(id=tweet_id)

def like_a_punny_tweet():
    like_tweet("1171113632362577922")