import psycopg2
from config import Config

def get_all_albums() -> list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM album where deleted_at is null"
    # val = (email,)
    mycursor.execute(sql)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_album_by_id(id: int) -> dict:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM album WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_album_by_code(code:str)->dict:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM album WHERE code = %s"
    val = (code,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_albums_by_artist(artist_id: int)->list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM album where artistId = %s"
    val = (artist_id,)
    mycursor.execute(sql,val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None
