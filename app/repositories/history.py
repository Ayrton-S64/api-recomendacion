import psycopg2
from config import Config

def get_history_by_user_id(user_id: int) -> list:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM Reproduccion WHERE usuarioId = %s AND deleted_at is null"
    val = (user_id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None
