# Fetch Trending Topic(s) from Twitter and create video around that and upload in Youtube
_________
## Fetch Tredning Topics
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
----
Refrences Code used from:
-[text_processing.clean_text.py](https://gist.github.com/MrEliptik/b3f16179aa2f530781ef8ca9a16499af?permalink_comment_id=3970601) ((used almost as it is))
