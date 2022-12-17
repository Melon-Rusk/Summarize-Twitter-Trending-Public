import requests
import json
import base64

API_KEY = "YOUR_API_KEY"
CHANNEL_ID = "YOUR_CHANNEL_ID"
VIDEO_FILE = "path/to/video.mp4"

metadata = {
    "snippet": {
        "title": "My Awesome Video",
        "description": "This is an awesome video that I made.",
        "categoryId": 22
    },
    "status": {
        "privacyStatus": "private"
    }
}

def upload_youtube_video(API_KEY, VIDEO_FILE, metadata):
    url = f"https://www.googleapis.com/upload/youtube/v3/videos?part=snippet,status&key={API_KEY}" 

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

    with open(VIDEO_FILE, "rb") as f:
        video_data = f.read()
    video_data = base64.b64encode(video_data).decode("ascii")

    payload = {
    "snippet": metadata["snippet"],
    "status": metadata["status"],
    "videoFile": video_data
}

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Video uploaded successfully")
    else:
        print("Error uploading video:", response.text)

upload_youtube_video(API_KEY, VIDEO_FILE, metadata)




if __name__ == "__main__":
    pass
