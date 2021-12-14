import os

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

CLIENT_SECRETS_FILE = 'client_secret.json'

SCOPES = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def get_my_uploads_list():
    channels_response = youtube.channels().list(
        mine=True,
        part='contentDetails'
    ).execute()

    for channel in channels_response['items']:
        return channel['contentDetails']['relatedPlaylists']['uploads']

    return None


def list_my_uploaded_videos(uploads_playlist_id):
    playlistitems_list_request = youtube.playlistItems().list(
        playlistId=uploads_playlist_id,
        part='snippet',
        maxResults=5
    )

    videos_ids = []
    while playlistitems_list_request:
        playlistitems_list_response = playlistitems_list_request.execute()

        for playlist_item in playlistitems_list_response['items']:
            video_id = playlist_item['snippet']['resourceId']['videoId']
            videos_ids.append(video_id)

        playlistitems_list_request = youtube.playlistItems().list_next(
            playlistitems_list_request, playlistitems_list_response)
    return videos_ids

def get_video_rating(youtube, id):
    video_data = youtube.videos().list(id=id, part='statistics').execute()
    return video_data['items'][0]['statistics']['dislikeCount']

def edit_description(dislikes, description:str):
    if "Acest video are" in description and " Dislikes 👎\nSe actualizează în fiecare zi..." in description:
        description = description[description.index('Se actualizează în fiecare zi...')+len('Se actualizează în fiecare zi...'+"\n\n"):]
    return "Acest video are "+ dislikes +" Dislikes 👎\nSe actualizează în fiecare zi..." + "\n\n" + description

def update_video(youtube, id):
    videos_list_response = youtube.videos().list(
        id=id,
        part='snippet'
    ).execute()
    videos_list_snippet = videos_list_response['items'][0]['snippet']

    rating = get_video_rating(youtube, id)
    videos_list_snippet['description'] = edit_description(rating, videos_list_snippet['description'])

    youtube.videos().update(
        part='snippet',
        body=dict(
            snippet=videos_list_snippet,
            id=id
        )).execute()


if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    youtube = get_authenticated_service()

    try:
        uploads_playlist_id = get_my_uploads_list()
        if uploads_playlist_id:
            videos_ids = list_my_uploaded_videos(uploads_playlist_id)
        else:
            print('There is no uploaded videos playlist for this user.')
    except HttpError as e:
        print(f'An HTTP error {e.resp.status} occurred:\n{e.content}')

    for id in videos_ids:
        update_video(youtube, id)

    print(f"{len(videos_ids)} videoclipuri au fost actualizate cu succes!")