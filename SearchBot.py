# Mainly created for ReTweeting by bot for a particular Tweet

import tweepy
import time

consumer_key = 'ZNBMfwAja9DoBkdhyOpSwdoQb'
consumer_secret = 'HoJGyXH2lxPvXFrxIoGxzjRBYu9iOAzFVRUljlq6RSSkcePJpN'
key = '1363564975625805825-iii4q7lQpsVmsSs2uNH2wQWzxmdWso'  #Access token
secret = 'BSg8L2IFoQzc8si8hR8oJ0mwhHaCKWf4QtSmeORnXJRLg' #Access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret) # taking tokens and

api = tweepy.API(auth)
#tweepy is a object where as cursor is a method

hashtag = '#CodeisLife'      # Tweet containing this hashtag will be Retweeted
tweetNumber = 1              # TweetNumber can be vary with different tweets
tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Done with ReTweet !!")
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

searchbot()