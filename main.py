import requests
import urllib.request

def get_top_twitch_clips(client_id, access_token, game_id, limit=10):
    url = f"https://api.twitch.tv/helix/clips?game_id={game_id}&first={limit}"
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    clips = response.json()['data']
    return clips
def download_clip(clip_url, file_name):
    urllib.request.urlretrieve(clip_url, file_name)

