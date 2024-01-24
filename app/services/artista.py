from app.repositories.song import get_songs_by_artist
from app.repositories.album import get_albums_by_artist, get_album_by_id
from app.repositories.artista import get_all_artists,get_artist_by_id

def get_all() -> list:
    try:
        # Find user by email
        artists = get_all_artists()

        # for artist in artists:
        #   artist['album'] = get_albums_by_artist(artist['id'])
        #   artist['artist'] = get_songs_by_artist(artist['id'])
            
        print(artists)        

        return artists
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def get_by_id(artist_id: int) -> dict:
  try:
      # Find user by email
      artist = get_artist_by_id(artist_id)
      artist['album'] = get_albums_by_artist(artist_id)
      artist['artist'] = get_songs_by_artist(artist_id)
      print(artist)        

      return artist
  except Exception as e:
      # Log the exception or handle it in a way that makes sense for your application
      print(f"An error occurred: {e}")
      # Optionally, re-raise the exception if needed
      raise

def get_songs(artist_id)->list:
    try:
        # Find user by email
        songs = get_songs_by_artist(artist_id)
        for song in songs:
          song['album'] = get_album_by_id(song['albumId'])
          song['artist'] = get_artist_by_id(song['artistaId'])
            
        print(songs)        

        return songs
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def get_albums(artist_id)->list:
    try:
        # Find user by email
        albums = get_albums_by_artist(artist_id)

        # for artist in artists:
        #   artist['album'] = get_albums_by_artist(artist['id'])
        #   artist['artist'] = get_songs_by_artist(artist['id'])
            
        print(albums)        

        return albums
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def get_recomendations(number: int)->list:
    pass
