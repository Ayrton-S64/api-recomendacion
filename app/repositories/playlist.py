import psycopg2
from config import Config

def get_all_playlists() -> list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM ListaReproduccion where deleted_at is null"
    # val = (email,)
    mycursor.execute(sql)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_playlist_by_id(id: int) -> dict:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM ListaReproduccion WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_playlist_by_user(user_id: int)->list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM ListaReproduccion where usuarioId = %s"
    val = (user_id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None
    
def get_playlist_songs(id: int)->list:
  mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
  mycursor = mydb.cursor(dictionary=True)
  sql = "SELECT * FROM CancionListaReproduccion where listaReproduccionId = %s deleted_at is null"
  val = (id,)
  mycursor.execute(sql, val)
  
  result = mycursor.fetchall()
  
  mycursor.close()
  mydb.close()
  if result:
      return result
  else:
      return None