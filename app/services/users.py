from app.repositories.users import get_user_by_id, get_user_by_email
from app.repositories.playlist import get_playlist_by_user

def get_by_id(user_id: int) -> dict:
  try:
      # Find user by email
      user = get_user_by_id(user_id)

      print(user)       

      return user
  except Exception as e:
      # Log the exception or handle it in a way that makes sense for your application
      print(f"An error occurred: {e}")
      # Optionally, re-raise the exception if needed
      raise

def get_by_email(user_email)->dict:
    try:
        # Find user by email
        user = get_user_by_email(user_email) 

        print(user)

        return user
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def get_playlists(user_id: int)->list:
    try:
        # Find user by email
        playlists = get_playlist_by_user(user_id) 

        print(playlists)

        return playlists
    except Exception as e:
        # Log the exception or handle it in a way that makes sense for your application
        print(f"An error occurred: {e}")
        # Optionally, re-raise the exception if needed
        raise

def get_recomendations(number: int)->list:
    pass
