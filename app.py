from flask import Flask, render_template  
import requests 

app = Flask(__name__)

access_token = 'BQB37bAXtOsq1PgzkpvlouSZQB7GzRHVdsva5C7lyVrnXnnVBaaeDszvsv3mrVrrlFA7HUifbsvPB0OJn3nOCM_IUKJtppdk9_go60RLd0C3b2AzlY4' 
headers = {
    'Authorization': f'Bearer {access_token}', 
    'Content-Type': 'application/json' 
}

ids_artist = [
    '6eUKZXaKkcviH0Ku9w2n3V',  # Ed Sheeran
    '1dfeR4HaWDbWqFHLkxsg1d',  # Queen
    '66CXWjxzNUsdJxJ2JdwvnR',  # Ariana Grande
    '04gDigrS5kc9YWfZHwBETP',  # Maroon 5
    '53XhwfbYqKCa1cC15pYq2q',  # Imagine Dragons
    '7dGJo4pcD2V6oG8kP0tJRR',  # Eminem
    '1HY2Jd0NmPuamShAr6KMms',  # Lady Gaga
    '4gzpq5DPGxSnKTe4SA8HAU',  # Coldplay
    '6vWDO969PvNqNYHIOW5v0m',  # Beyoncé
    '0du5cEVh5yTK9QJze8zA0C',  # Bruno Mars
    '5pKCCKE2ajJHZ9KAiaK11H',  # Rihanna
    '0EmeFodog0BfCgMzAIvKQp',  # Shakira
    '1uNFoZAHBGtllmzznpCI3s',  # Justin Bieber
    '6S2OmqARrzebs0tKUEyXyp',  # Dua Lipa
    '06HL4z0CvFAxyc27GXpf02'   # Taylor Swift
]

def get_artist_data(artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}'  
    response = requests.get(url, headers=headers) 
    if response.status_code == 200:
        return response.json() 
    else:
        print(f"Erro ao buscar dados do artista com ID {artist_id}: {response.status_code}")  

def get_artist_data_all():
    data = []  
    for id_artist in ids_artist:  
        data_artist = get_artist_data(id_artist) 
        if data_artist:  
            data.append(data_artist)  
    return data 

def get_artists_pop(artists_data):
    pop_artists = []
    for artist in artists_data:
        if 'genres' in artist:
            if 'pop' in artist['genres']:
                artist_info = {
                    'artist_name': artist['name'],
                    'followers': artist['followers']['total']
                }
                pop_artists.append(artist_info)
    sorted_artists = sorted(pop_artists, key=lambda artist: artist['followers'], reverse=True)
    final_pop_artists = []
    for artist in sorted_artists:
        final_pop_artists.append(artist)
    return final_pop_artists

def  get_equal_genres(artists_data):
    genres_list = []
    for artist in artists_data:
        if 'genres' in artist:
            for genre in artist['genres']:
                genres_list.append(genre)
    from collections import Counter
    genre_count = Counter(genres_list)
    equal_genres_list = []
    for genre, _ in genre_count.most_common(5):
        equal_genres_list.append(genre)
    return equal_genres_list

@app.route('/')
def index():
    artists_data = get_artist_data_all()
    pop_artists_ranking = get_artists_pop(artists_data)  
    genre_ranking = get_equal_genres(artists_data) 
    return render_template('index.html', pop_artists=pop_artists_ranking, common_genres=genre_ranking)

if __name__ == '__main__':
    app.run(debug=True) 
