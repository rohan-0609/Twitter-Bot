# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import tweepy
import time

consumer_key = 'ZNBMfwAja9DoBkdhyOpSwdoQb'
consumer_secret = 'HoJGyXH2lxPvXFrxIoGxzjRBYu9iOAzFVRUljlq6RSSkcePJpN'
key = '1363564975625805825-iii4q7lQpsVmsSs2uNH2wQWzxmdWso'  #Access token
secret = 'BSg8L2IFoQzc8si8hR8oJ0mwhHaCKWf4QtSmeORnXJRLg' #Access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret) # taking tokens and

api = tweepy.API(auth)

File_Name = 'last_seen.txt'

#Reading the last tweet added in your twitter account

def read_last_seen(File_Name):
    file_read = open(File_Name, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id
#Storing the last seen weer and tweet id in a txt file

def store_last_seen(File_Name, last_seen_id):
    file_write = open(File_Name, "w")
    file_write.write(str(last_seen_id))
    file_write.close()

def reply():
    tweets = api.mentions_timeline(read_last_seen(File_Name), tweet_mode='extended')

    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("================")
            print("New Tweet found!")
            print("Replied to ID- " +str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + "  I'm good, and I have finished the project already !!!", tweet.id) # replying a tweet, asked on the seocnd account
            api.create_favorite(tweet.id) # To make a tweet liked or loved(method which hits a particular tweet loved
            api.retweet(tweet.id)
            store_last_seen(File_Name, tweet.id)
while True:
    reply()
    time.sleep(15)