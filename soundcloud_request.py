# NOTE: DOESN'T WORK BCS SOUNDCLOUD DOESN'T ACCEPT ANY NEW APPS
# NOTE: LEAVING CODE HERE IN CASE WE USE IT LATER ON (UNLIEKLY)

import requests

def fetch_track_info():
    url = "https://api.soundcloud.com/tracks"
    client_id = 'd57e5ff839cb48d7bcb73016f0b6acb9'
    
    params = {
        'client_id': client_id,
        'limit': 20,
        'order': 'created_at'
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching data from SoundCloud: {response.status_code}")
        return []

    tracks_data = response.json()
    
    track_info_list = []
    for index, track in enumerate(tracks_data):
        title = track['title']
        artist_name = track['user']['username']
        release_date = track.get('release_year', 'N/A')
        album_name = track.get('album', 'N/A')
        genre = track.get('genre', 'Unknown Genre')
        stream_count = track.get('playback_count', 0)
        sound_cloud_url = track['permalink_url']
        
        track_info_list.append({
            "rank": index + 1,
            "title": title,
            "artist_name": artist_name,
            "release_date": release_date,
            "album_name": album_name,
            "genre": genre,
            "stream_count": stream_count,
            "sound_cloud": sound_cloud_url
        })
    
    return track_info_list

if __name__ == "__main__":
    track_info = fetch_track_info()
    
    for info in track_info:
        print(info)
