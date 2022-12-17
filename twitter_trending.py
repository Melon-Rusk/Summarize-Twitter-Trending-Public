import tweepy
import config.config as config
import sys
import json
from api_modules.twitter_api import refresh_access_token

API_KEY = config.API_KEY
API_SECRET = config.API_SECRET_KEY

# Authenticate with Twitter
def get_trending_list(API_KEY, API_SECRET):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET) # type: ignore
    # Create an API object
    api = tweepy.API(auth) # type: ignore

    # Fetch the current trending topics
    trending_topics = api.trends_place(1)

    # with open('store_data/trending_topic.pickle','wb') as f1:
    #     pickle.dump(trending_topics,f1)
    # Print the trending topics
    for topic in trending_topics:
        print(topic['name'])
    return trending_topics

def get_trending_topics():

    #Autenticações
    consumer_key = ''
    consumer_secret = ''
    access_token = refresh_access_token()
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #type: ignore
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth) #type: ignore

    # Where On Earth ID for Brazil is 23424768.
    BRAZIL_WOE_ID = 23424768

    brazil_trends = api.trends_place(BRAZIL_WOE_ID)

    trends = json.loads(json.dumps(brazil_trends, indent=1))

    for trend in trends[0]["trends"]:
        print (trend["name"]).strip("#") #type: ignore



if __name__ == '__main__':
    get_trending_list(API_KEY, API_SECRET)
