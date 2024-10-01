from googleapiclient.discovery import build
from google.oauth2 import service_account

def upload_to_youtube(video_file, title, description, category_id="24", privacy_status="public"):
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    SERVICE_ACCOUNT_FILE = "path_to_your_service_account.json"

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    youtube = build('youtube', 'v3', credentials=credentials)
    
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['Twitch', 'Shorts'],
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': privacy_status
        }
    }
    
    media = MediaFileUpload(video_file)
    
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )
    response = request.execute()
    return response
