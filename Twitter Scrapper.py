#Importing libraries
import pandas as pd 
import numpy as np 
import tweepy as tw
import csv

#Access Keys 
consumer_key='*****************'
consumer_secret='*****************'
access_token='*****************'
access_token_secret='*****************'

#Function to scrap tweets
search_word=' '
def scrapper(search_word,count):
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    tweets = tw.Cursor(api.search,q=search_word + " -filter:retweets",lang='en').items(count)
    df=pd.DataFrame([tweet.text for tweet in tweets],columns=['Tweets'])
    #Uncomment to store it in CSV
    #data=df.to_csv("Enter the required file path")
    return(df)
