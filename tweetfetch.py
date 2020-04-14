import tweepy 
import pandas as pd 
import preprocess
import MLmodel

# stub function
import random

consumer_key = "L2qFoCZWuzrAeNgu9jWXuR11Z"
consumer_secret = "BkbJyNa90JKEKeFhkGQ2yKDaMG7geOxuBsrCMwz1oOt0zQF7By"
access_key = "1221670879999885312-oXJPV5PJJihL3A5bj6fFyjd7uLaZ5X"
access_secret = "FUDpsoNcnhAjEhLh0R3kiqucms8Rp60Isg0XrrxFtkuMQ"


def get_tweets(username): 
		
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

		auth.set_access_token(access_key, access_secret) 

		api = tweepy.API(auth) 
		
		tweets = api.user_timeline(screen_name=username,  count = 200, exclude_replies=1) 

		tmp=[] 

		tweets_for_csv = [tweet.text for tweet in tweets] 
		for j in tweets_for_csv: 
			tmp.append(j) 

		print("\n\nUSERNAME- " ,username)
		df = pd.DataFrame(tmp)
		df.columns = ["Tweets"]

		# preprocessing (refer preprocess.py)
		preprocess.preprocess(df)

		#use ml model
		return MLmodel.findCategory(df)

		#this is to situmate the value/category the ML model has returned.
		#We might need to return more values in an object like number of tweets analyzed and no of tweets in each category for analytics.

if __name__ == '__main__':
    get_tweets('iamsrk')
		

