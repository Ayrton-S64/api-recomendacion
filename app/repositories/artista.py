import psycopg2
from config import Config

def get_all_artists() -> list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM artista where deleted_at is null"
    # val = (email,)
    mycursor.execute(sql)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_artist_by_id(id: int) -> dict:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM Artista WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None