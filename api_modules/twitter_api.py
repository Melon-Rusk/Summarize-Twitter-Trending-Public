import requests
import pickle
from pathlib import Path
import sys
import re
import os
import geocoder
import tweepy
from tweepy import OAuthHandler #type: ignore
import json
# from datetime import datetime
import datetime
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import config


# sys.path.append(os.path.dirname(__file__))

def refresh_access_token():
    url = "https://api.twitter.com/oauth2/token"

    payload = 'grant_type=client_credentials'
    headers = {
        'Authorization': f'Basic {config.TWITTER_REFRESH_TOKEN}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.json()['access_token']


def load_access_token():
	# load access token from file
	with open('store_data/access_token.pickle', 'wb') as f1:
		access_token = pickle.load(f1)
	return access_token


def get_tweets_from_id(id: str)->dict:

	url = f"https://api.twitter.com/2/tweets?ids={id}"
	payload = {}
	headers = {'Authorization': f'Bearer {config.BEARER_TOKEN}'}

	response = requests.request("GET", url, headers=headers, data=payload)

	print(response.text)
	return response.json()['data'][0]['text']

def get_auth():
    auth = OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    return auth

def save_trends(trends,loc):
	folder = f"{str(Path(__file__).resolve().parent.parent)}\\store_data"
	loc = str(loc)
	loc = re.sub('[^0-9a-zA-Z]+', '_', loc)
	time = datetime.datetime.now()
	time = re.sub('[^0-9a-zA-Z]+', '_', str(time))
	file_name = f"{folder}\\trends_time_{time}_loc_{loc}.json"
	with open(file_name,"w") as f1:
		json.dump(trends,f1)


def get_trends(loc):
	# auth =  # type: ignore   
	auth = get_auth()
	api = tweepy.API(auth) # type: ignore    
	# Object that has location's latitude and longitude.
	if type(loc) == str:
		g = geocoder.osm(loc)
		lat = g.lat
		long = g.lng
	else:
		lat = loc[0]
		long = loc[1]
	closest_loc = api.closest_trends(lat, long)
	trends = api.get_place_trends(closest_loc[0]["woeid"])
	# trending = 	json.dumps(, indent=4)
	trending = trends[0]["trends"]
	save_trends(trending,loc)
	
	return trending


def get_tweet_from_text(text, start_time, end_time,next_token ='',max_tweets = 100,counter=1):
	data = []
	search_url = "https://api.twitter.com/2/tweets/search/recent"
	text = re.sub('[^0-9a-zA-Z$]+', '',text)
	url = f"{search_url}?query={text}&start_time={start_time}&end_time={end_time}&max_results={max_tweets}&tweet.fields=lang"
	if len(next_token)>5:
		url = f"{url}&next_token={next_token}"

	payload={}
	headers = {
	'Authorization': f'Bearer {config.BEARER_TOKEN}'}

	response = requests.request("GET", url, headers=headers, data=payload)

	if response.status_code == 200:
		# response.json
		data = response.json().get('data')
		next_token = response.json()['meta'].get('next_token',"End")
		if counter<6 and next_token != 'End':
			counter = counter+1
			print(f"Attempt in get_tweet_from_text {counter}")
			data_temp = get_tweet_from_text(text, start_time, end_time,next_token =next_token,max_tweets = 100,counter=counter)
			data = data + data_temp
		return data 
	return data 





def main():
	get_tweets_from_id('1601569532782735361')
	text ='IshanKishan'
	# start_time = '2022-12-10T12:48:14.743810+00:00'
	# start_time = '2022-12-09T15:29:28.972488Z'
	end_time = '2022-12-10T12:29:28.972488Z'

	end_time = (datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(seconds=30)).isoformat().replace("+00:00","Z")
	start_time=(datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(hours=2)).isoformat().replace("+00:00","Z")
	response = get_tweet_from_text(text, start_time, end_time)

	if True:
		loc = (25.24, 85.6)
	else:
		loc = input("Enter the location name")
	# trends = get_trends(loc)
	# print(json.dumps(trends, indent=4))






if __name__ == '__main__':
	# refresh_token()
	main()