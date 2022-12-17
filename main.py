
import pickle
import pandas as pd
import datetime
import re
import json
from twiter_trending_summary import fetch_trending_topics_text
from create_text_summary import  summarize_text
from summarize_abstractive import abstract_summary
from video_editing.create_video import creat_video_animation
from moviepy.editor import VideoFileClip,concatenate_videoclips
from api_modules.youtube_client_lib_upload import upload_video_yt

def get_trending_topic(location="India"):
    df = pd.DataFrame(columns=['topic','sentiment','abstract_summary'])
    if True:
        text_list = fetch_trending_topics_text(loc=location,lang='en',top=20)
    else:
        path = 'store_data\\trend_data\\list_dict.pickle'
        with open(path,"rb") as f1:
            text_list= pickle.load(f1)
    text_list_new = []
    min_text_length = 0  
    for text in text_list:
        if len(text)>min_text_length: #type: ignore
            text["short_summary"] = summarize_text(text["summary"])
            if len(text["short_summary"])>50:
            # text['short_summary'] = summarize_text(text["summary"])
                max_length = int(min(len(text["summary"])/10,200))
                text['abstract_summary'] = abstract_summary(text["short_summary"],max_length=max_length)
            elif len(text["short_summary"])>5:
                text['abstract_summary'] = abstract_summary(text["short_summary"],max_length=5)
            else:
                text['abstract_summary'] = text["summary"]

            text_list_new.append(text)
    if len(text_list_new)>0:
        df = pd.json_normalize(text_list_new)
        date_time = re.sub('[^0-9a-zA-Z]+', '_',str(datetime.datetime.now()))
        # df.apply(lambda x: x.str.replace(',',' '))
        # df.to_csv(f"store_data/twitter_trending_summary_{date_time}.csv",sep=",")
        df_dict = df.to_dict('records')
        with open(f"store_data/twitter_trending_summary_{date_time}.json","w") as f1:
            json.dump(df_dict,f1)
        df_dict_summary = df[['topic','sentiment','abstract_summary']].to_dict('records')

        with open(f"store_data/twitter_trending_short_summary_{date_time}.json","w") as f1:
            json.dump(df_dict_summary,f1)
    return df[['topic','sentiment','abstract_summary']]

def get_final_video(location):
    if True:    
        df = get_trending_topic(location)
        if len(df)<1:
            raise Exception("Insufficient Data")
    else:
        with open(f'store_data\\trend_data\\twitter_trending_short_summary_2022_12_11_01_05_11_774027.json',"r") as f1:
            df_dict = json.load(f1)
        df = pd.json_normalize(df_dict)#.head(2)
    df['video_filename'] = ''
    tags = list(df['topic'].unique())
    discription = ''
    for i in range(len(df)):
        heading = df['topic'].iloc[i]
        sentiment = df['sentiment'].iloc[i]
        summary = df['abstract_summary'].iloc[i]
        discription = discription +f'''\n\n{heading} : {summary}'''
        print(f"""heading: {heading},
                sentiment:{sentiment},
                summary: summary""")

        file_name = f"{location}_summary_11_Dec_2022"
        df['video_filename'].iloc[i] = creat_video_animation(heading,summary,file_name)
        # i = i+1

    file = 'store_data\\video_disclaimer_video_disclaimer_.mp4'
    video_clips = [VideoFileClip(file)]
    if len(df)>0:
        for i in range(len(df)):
            file = df['video_filename'].iloc[i]
            video_clips.append(VideoFileClip(file))
            i = i+1
    else: 
        raise Exception("Insufficient Data")


    final_clip = concatenate_videoclips(video_clips, method="compose")

    time = str(datetime.datetime.now())
    time = re.sub("[^0-9a-zA-Z]+","_",time)
    final_video_file_name = f"store_data\\final_video\\concatenated_video_{time}.mp4"
    final_clip.write_videofile(final_video_file_name)
    return final_video_file_name, tags,discription

if __name__ == "__main__":
    location = "India"
    final_video_file_name, tags,discription = get_final_video(location)
    privacy = 'unlisted'    
    link = upload_video_yt(final_video_file_name,tags ,discription,privacy,location)

    print(link)
    print("XYZ")

