# Create Engaging YouTube Videos from Twitter's Trending Topics
## Introduction
This project allows you to easily fetch the trending topics on Twitter for a given location, create a summary for each topic, generate a video using Google Text-to-Speech and OpenCV, merge all the videos into one, and upload the final video to YouTube. You can use this project to quickly and easily create engaging content for your YouTube channel.
## [GitHub Repo](https://github.com/Melon-Rusk/Summarize-Twitter-Trending-Public)

## Features
- Fetch trending topics from Twitter using the Tweepy and geocoder libraries
- Create a summary for each trending topic using the Tweepy, nltk, and transformers libraries
- Generate a video using the gtts, cv2 (OpenCV), and moviepy libraries
- Concatenate multiple videos into one using moviepy
- Upload the final video to YouTube using the googleapiclient library

## Dependencies
- Tweepy
- geocoder
- nltk
- transformers
- gtts
- cv2 (OpenCV)
- moviepy
- googleapiclient

## Quick Start
1. Clone the repository:  
```
git clone https://github.com/Melon-Rusk/Summarize-Twitter-Trending-Public
```
2. Navigate to the project directory: 
```
cd Summarize-Twitter-Trending-Public
```
3. Install the dependencies: 
```
pip install -r requirements.txt
```
4. Update the credentials in the config file.
5. Run the project: 
```
python main.py
```

_________

## Fetch Trending Topics
- Fetch Trending Topics for the given location
- Library used: *Tweepy*, *geocoder*

## Create summary for the each trending topics
- Fetch Tweets related to text (from last 2hr)
- Filter tweets of specified language
- Clear tweets remove emojis, urls, punctutations, stopwords
- Generate Sentiment
- Create Extract summary from the text
- Clean text remove ascii characters and remove urls
- Create abstract summary from the extracted summary
- Library module/used: *Tweepy*,*nltk*,*transformers*

## Generate Video
- Generate Audio from text using google text to speech
- Generate Image from text using open cv
- Generate Video using audio and image
- Library/modules used: *gtts*,*cv2 (opencv)*, *moviepy*

## Concatenate Videos
- For merge video for each trending topic in to one
- Library/modules used: *moviepy*

## Upload video on YT
- Using Twitter trending topics as Tags
- And summary as description
- Using Youtubes's library upload video on youtube
- Library/Modules used: *googleapiclient*

----
# Update Credentials in config to test it
Refrences Code used from:
-[text_processing.clean_text.py](https://gist.github.com/MrEliptik/b3f16179aa2f530781ef8ca9a16499af?permalink_comment_id=3970601) (used almost as it is)


