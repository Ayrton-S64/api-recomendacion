from app.repositories.artista import get_artist_by_id
from app.repositories.album import get_album_by_id
from app.repositories.song import get_songs_by_album
from app.repositories.album import get_all_albums, get_album_by_code

def get_all() -> list:
    try:
        albums = get_all_albums()

        for album in albums:
          album['artist'] = get_artist_by_id(album['artistaId'])
            
        print(albums)        

        return albums
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def get_by_code(album_code: str) -> dict:
  try:
      # Find user by email


      
      album = get_album_by_code(album_code)
      album['artist'] = get_artist_by_id(album['artistaId'])
      album['songs'] = get_songs_by_album(album['id'])
      print(album)        

      return album
  except Exception as e:
      # Log the exception or handle it in a way that makes sense for your application
      print(f"An error occurred: {e}")
      # Optionally, re-raise the exception if needed
      raise

def get_songs(album_id)->list:
    try:
        # Find user by email
        songs = get_songs_by_album(album_id)

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

def get_recomendations(number: int)->list:
    pass
