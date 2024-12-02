import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

def fetch_raw_track_info(playlist_id):
    client_id = '9ccfa603b1e44e4d83df5e07d118dcc8'
    client_secret = '95f173867e00467991ca93235f4c1ed8'
    
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # Fetch playlist tracks data
    tracks_data = sp.playlist_tracks(playlist_id=playlist_id, limit=100)
    return tracks_data

def save_raw_to_file(data, filename="SpotifySongs12.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        # Save raw JSON data with indentation for readability
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Raw data saved to {filename}")

if __name__ == "__main__":
    playlist_id = '0QXFfy6gn85CnyYDYcND4z'
    raw_data = fetch_raw_track_info(playlist_id)
    save_raw_to_file(raw_data)
