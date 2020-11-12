# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:33:28 2020

@author: Kevin
"""

import tweepy
consumer_key = "JoPmGvLluEyLqyASsz49lE0fh"
consumer_secret = "sOcYXKBtnWYtIkzjiYS2tw9y7OdeX2qcP3SnZk8FYe5kzLz2ME"
access_token = "1287763964466610176-K64Z6DDuzE8zLWvH0vn5Q8Nz6d13b1"
access_token_secret = "ZLA10vZWo27ervw0DgCGLKpWsZ35GtEcmC9ploOqMbKdM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
    
nama = "jokowi"
jumlah_tweet = 100
hasil = api.user_timeline(id=nama, count=jumlah_tweet)
count_covid = 0

for tweet in hasil:
    post = tweet.text.lower()
    if("covid" in post):
        count_covid+=1

print("banyak tweet pak jokowi yang diambil: ",str(jumlah_tweet))
print("banyaknya pak jokowi membicarakan Covid dalam tweetnya: ",str(count_covid))