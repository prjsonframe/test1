import requests
import os

GITHUB_USER = 'prjsonframe'
GITHUB_REPO = 'test1'
BRANCH = 'main'  # or 'master'
SONGS_DIR = 'songs'
LOCAL_DIR = './songs'

ARTISTS = ['Tame Impala', 'Kanye West', 'Travis Scott']

SONGS = {
    'Tame Impala': ['dark-engine-logo-141942.mp3', 'short-modern-logo-242225.mp3'],
    'Kanye': ['short-kiss-96901.mp3', 'short-round-110940.mp3'],
    'Travis': ['deep-strange-whoosh-183845.mp3', 'short-modern-logo-242224.mp3'],
    # Add more as needed
}

def fetch_and_save(artist, song):
    url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/{SONGS_DIR}/{artist}/{song}"
    local_artist_dir = os.path.join(LOCAL_DIR, artist)
    os.makedirs(local_artist_dir, exist_ok=True)
    local_path = os.path.join(local_artist_dir, song)
    print(f"Downloading {artist} - {song}...")
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(local_path, 'wb') as f:
            f.write(resp.content)
        print(f"Saved {local_path}")
    else:
        print(f"ERROR: {url} not found (status {resp.status_code})")

for artist in ARTISTS:
    for song in SONGS[artist]:
        fetch_and_save(artist, song)
