import psycopg2
from config import Config

def get_user_by_email(email: str) -> dict:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM usuario WHERE correo = %s"
    val = (email,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchone()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def get_user_by_id(user_id: int)->dict:
    mydb = psycopg2.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )
    
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM usuario WHERE id = %s"
    val = (user_id,)
    mycursor.execute(sql, val)
    
    result = mycursor.fetchone()
    
    mycursor.close()
    mydb.close()
    if result:
        return result
    else:
        return None

def insert_user(username: str, email:str, password: str) -> bool:
  try:
    mydb = psycopg2.connector.connect(
        host=Config.POSTGRESQL_HOST,
        user=Config.POSTGRESQL_USER,
        password=Config.POSTGRESQL_PASSWORD,
        database=Config.POSTGRESQL_DATABASE
    )

    cursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO usuario (username, email, password) VALUES (%s,%s,%s)"
    val = (username, email, password)
    cursor.execute(sql,val)

    mydb.commit()
    cursor.close()
    mydb.close()

    return True
  except Exception as e:
    print(f"An error occurred while inserting user: {e}")
    raise

def update_user(username: str, password: str)->bool:
   pass