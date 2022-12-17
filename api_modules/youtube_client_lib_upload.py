
import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import re

CLIENT_SECRET_FILE = 'config\client_secret_yt.json'
YOUTUBE_SCOPE = ['https://www.googleapis.com/auth/youtube']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


creds = Credentials.from_authorized_user_file(CLIENT_SECRET_FILE, YOUTUBE_SCOPE)
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=creds)
disclaimer = """This video is created using crowd sourced data and has not been reviewed to avoid bias. As such, it may contain incorrect information. Please let us know if you find any errors or omissions. The information and views expressed in this video are not necessarily those of the creator and are for educational and entertainment purposes only. The creator cannot be held responsible for any damages or losses arising from the use of the information provided"""

def upload_video_yt(file_path,tags:list,discription:str="",privacy:str="private",location="India"):
    try:
        discription = re.sub(r'http\S+', '', discription)
        discription = re.sub(r'//t.co+', '', discription)
        discription = re.sub(r'@+',' ',discription)
        discription = re.sub(r'\n',' ',discription)
        location = location.capitalize()
        discription_tags = discription.split("#")
        discription_tag_list = []
        for t in discription_tags:
            discription_tag_list.append(t.strip().split(" ",1)[0])# = discription_tag_str + " #"+t.strip().split(" ",1)[0]
        discription_tag_list = list(set(discription_tag_list))
        discription_tag_str = "#"+ ", #".join(discription_tag_list)
        discription_tag_str = discription_tag_str.replace(":","")
        # Create a request object to upload the video to YouTube
        # file_path = 'store_data\\final_video\\concatenated_video_2022_12_11_21_29_04_849260.mp4'
        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": f"Todays twitter Summary | {location} |{datetime.datetime.today().strftime('%Y-%m-%d')}",
                    "description": f"""This video is summary of {datetime.datetime.today().strftime('%Y-%m-%d')} twitter's trending
                    and is created without any human intervation so please let us know in case of any incorrect information, \n
                    {discription_tag_str}""",
                    "tags": tags,
                    "categoryId": 25
                },
                "status": {"privacyStatus": privacy}
            },
            media_body=MediaFileUpload(file_path, chunksize=-1, resumable=True)
        )
        response = request.execute()
        print(response)
        print(f'Video uploaded! URL: https://www.youtube.com/watch?v={response["id"]}')
        return f'''https://www.youtube.com/watch?v={response["id"]}'''
    except HttpError as error:
        print(f'An error occurred while uploading the video: {error}')
        raise error
if __name__ == "__main__":
    tags = ['Morocco', 'Ronaldo', 'FIFAWorldCup', 'Africa', 'GOAT', 'Tina', 'Semis', 'MARPOR', 'taehyun', 'Bono']
    file_path = 'store_data\\final_video\\concatenated_video_2022_12_11_21_29_04_849260.mp4'
    upload_video_yt(file_path,tags ,discription="")

