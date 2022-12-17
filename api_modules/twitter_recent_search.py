import requests
import os
import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import config
bearer_token = config.BEARER_TOKEN
import datetime
import requests


def get_tweet_from_text(text, start_time, end_time,next_token ='',max_tweets = 100,counter=1):
    data = []
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    url = f"{search_url}?query={text}&start_time={start_time}&end_time={end_time}&max_results={max_tweets}"
    if len(next_token)>5:
        url = f"{url}&next_token={next_token}"

    payload={}
    headers = {'Authorization': f'Bearer {config.BEARER_TOKEN}'}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    if response.status_code == 200:
        # response.json
        data = response.json()['data']
        next_token = response.json()['meta']['next_token']
        if counter<6:
            counter =counter +1
            data_temp = get_tweet_from_text(text, start_time, end_time,next_token =next_token,max_tweets = 100,counter=counter)
            data = data + data_temp
        return data 

def main():
    text ='IshanKishan'
    # start_time = '2022-12-10T12:48:14.743810+00:00'
    # start_time = '2022-12-09T15:29:28.972488Z'
    end_time = '2022-12-10T12:29:28.972488Z'
    
    end_time = (datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(seconds=30)).isoformat().replace("+00:00","Z")
    start_time=(datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(hours=2)).isoformat().replace("+00:00","Z")
    response = get_tweet_from_text(text, start_time, end_time)

if __name__ == "__main__":
    main()
    
