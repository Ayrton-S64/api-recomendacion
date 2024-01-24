from app.repositories.song import get_all_songs, get_song_by_code
from app.repositories.album import get_album_by_id
from app.repositories.artista import get_artist_by_id

def get_all() -> list:
    try:
        # Find user by email
        songs = get_all_songs()

        for song in songs:
          song['album'] = get_album_by_id(song['albumId'])
          song['artist'] = get_artist_by_id(song['artistId'])
            
        print(songs)        

        return songs
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def get_by_code(song_code: str) -> dict:
  try:
      # Find user by email
      song = get_song_by_code(song_code)
      song['album'] = get_album_by_id(song['albumId'])
      song['artist'] = get_artist_by_id(song['artistId'])
      print(song)        

      return song
  except Exception as e:
      # Log the exception or handle it in a way that makes sense for your application
      print(f"An error occurred: {e}")
      # Optionally, re-raise the exception if needed
      raise

def get_recomendations(number: int)->list:
    pass