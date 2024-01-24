from app.repositories.users import get_user_by_id
from app.repositories.album import get_album_by_id
from app.repositories.artista import get_artist_by_id
from app.repositories.playlist import get_all_playlists,get_playlist_by_id,get_playlist_songs

def get_all() -> list:
    try:
        # Find user by email
        playlists = get_all_playlists()

        for playlist in playlists:
          playlist['creator'] = get_user_by_id(playlist['usuarioId'])
            
        print(playlists)        

        return playlists
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def get_by_id(playlist_id: int) -> dict:
  try:
      # Find user by email
      playlist = get_playlist_by_id(playlist_id)
      playlist['creator'] = get_user_by_id(playlist['usuarioId'])
      playlist['songs'] = get_playlist_songs(playlist_id)
      print(playlist)        

      return playlist
  except Exception as e:
      # Log the exception or handle it in a way that makes sense for your application
      print(f"An error occurred: {e}")
      # Optionally, re-raise the exception if needed
      raise

def get_songs(playlist_id)->list:
    try:
        # Find user by email
        songs = get_playlist_songs(playlist_id)

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
