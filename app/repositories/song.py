import psycopg2
from config import Config

def get_all_songs() -> list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM cancion WHERE deleted_at is null"
    # val = (email,)

    mycursor.execute(sql)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_song_by_id(id: int) -> dict:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM cancion WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_song_by_code(code:str)->dict:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM cancion WHERE code = %s"
    val = (code,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_songs_by_artist(artist_id: int)->list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM cancion where artistId = %s"
    val = (artist_id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_songs_by_album(album_id: int)->list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM cancion where albumId = %s"
    val = (album_id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None