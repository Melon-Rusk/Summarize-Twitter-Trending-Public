import textblob
import json
import datetime
import re
import pickle
from api_modules.twitter_api import get_trends,get_tweet_from_text
import pandas as pd
from text_processing.clean_text import clean_text

def keep_english_trending_string(df):
    df['name_len'] = df['name'].str.len()
    df['name'] = df['name'].str.replace('[^a-zA-Z0-9]', '',regex=True)
    df['clean_name_len'] = df['name'].str.len()
    df['name_len_diff'] = df['name_len'] - df['clean_name_len']
    df = df[df['name_len_diff']<3]
    del df['name_len'] 
    del df['clean_name_len'] 
    del df['name_len_diff'] 
    return df

def fetch_trending_topics_text(loc="India",lang='en',top=2)->list[dict[str,str]]:
# authenticate with twitter API
    list_dict =[]
    # auth = get_auth()
    # api = tweepy.API(auth) # type: ignore    
    # get trending topics
    if False:
        file_path = 'store_data\\trends_time_2022_12_10_22_13_01_698663_loc_India.json'
        with open(file_path,'r') as f1:
            trending_topics = json.load(f1)
        # pass
    else:
        trending_topics = get_trends(loc)
    trending_topics = pd.json_normalize(trending_topics).fillna(0)
    trending_topics = trending_topics[trending_topics['promoted_content']==0]
    trending_topics = keep_english_trending_string(trending_topics)
    trending_topics = trending_topics.sort_values(by='tweet_volume',ascending=False).reset_index(drop=True)
    trending_topics = trending_topics.head(top)
    for topic in trending_topics['name']:
        summary = ""
        sentiment = 0
        # tweets = api.search(q=topic["name"][:top], lang="en")
        end_time = (datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(seconds=30)).isoformat().replace("+00:00","Z")
        start_time=(datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(hours=2)).isoformat().replace("+00:00","Z")
        tweets = get_tweet_from_text(topic, start_time, end_time)
        if tweets is not None and len(tweets)>0:
            for tweet in tweets:
                if 'RT' in tweet['text'][:2]:
                    if tweet['lang'] == lang:
                        tweet_text = tweet['text'].split(":")[1:]
                        tweet_text = " ".join(tweet_text)
                        tweet_text = clean_text(tweet_text)           
                    else:
                        tweet_text = ''
                else:
                    tweet_text = tweet['text']
                    tweet_text = clean_text(tweet_text)
                if tweet_text not in summary:
                    summary =summary+ " "+ tweet_text
                    summary = re.sub("  "," ",summary)
                    summary = summary.strip()
                    sentiment += textblob.TextBlob(tweet_text).sentiment.polarity
        temp_dict = {}
        print("Topic: ", topic)
        # print("Summary: ", summary)
        print("Sentiment: ", sentiment)
        print("\n")
        temp_dict["topic"] = topic
        temp_dict["summary"] = summary
        temp_dict["sentiment"] = sentiment
        list_dict.append(temp_dict)
    path = 'store_data\\list_dict.pickle'
    with open(path,"wb") as f1:
        pickle.dump(list_dict,f1)
    return list_dict

if __name__ == "__main__":
    location = "India"
    list_dict = fetch_trending_topics_text(location,lang='en',top=2)