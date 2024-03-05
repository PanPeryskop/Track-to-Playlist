import spotipy
from spotipy.oauth2 import SpotifyOAuth
import progressbar
import os
import configparser


def get_recommendations(track_id):
    results = sp.recommendations(seed_tracks=[track_id])
    tracks = []
    for track in results['tracks']:
        tracks.append(track['uri'])
    return tracks


def generate_playlist(track_id, times=5):
    all_tracks = []
    with progressbar.ProgressBar(max_value=times) as bar:
        for i in range(times):
            recommendations = get_recommendations(track_id)
            for track in recommendations:
                if track not in all_tracks:
                    all_tracks.append(track)
            bar.update(i)
    return all_tracks


config_file = 'config.sg'
config = configparser.ConfigParser()

if not os.path.exists(config_file):
    client_id = input("Enter your client_id: ")
    client_secret = input("Enter your client_secret: ")
    redirect_uri = input("Enter your redirect_uri: ")

    config['SPOTIFY'] = {'client_id': client_id, 'client_secret': client_secret, 'redirect_uri': redirect_uri}

    with open(config_file, 'w') as configfile:
        config.write(configfile)
else:
    config.read(config_file)
    client_id = config.get('SPOTIFY', 'client_id')
    client_secret = config.get('SPOTIFY', 'client_secret')
    redirect_uri = config.get('SPOTIFY', 'redirect_uri')

scope = 'playlist-read-private user-modify-playback-state playlist-modify-public playlist-modify-private user-top-read'
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

print("Enter the URL of the track: ")
url = input()

if url.startswith('https://open.spotify.com/track/'):
    number_of_characters = len(url)
    if number_of_characters == 73:
        track_id = url.split('/')[-1].split('?')[0]
    else:
        track_id = url.split('/')[-1]
else:
    print("Invalid URL.")
    exit()

playlist_name = input("Enter the name of the playlist: ")

playlist = generate_playlist(track_id)
playlist_spot = sp.user_playlist_create(sp.me()['id'], playlist_name, public=True)
playlist_id = playlist_spot['id']
track_ids = [track for track in playlist]
sp.playlist_add_items(playlist_id, track_ids)

print("Playlist created successfully.")
print(f"Playlist URL: https://open.spotify.com/playlist/{playlist_id}")
user_input = input()