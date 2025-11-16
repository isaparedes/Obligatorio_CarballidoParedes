import os
import pymysql
from pymysql.err import OperationalError

def get_connection():
    running_in_docker = os.environ.get("DOCKER") == "1"
    host = "mysql_container" if running_in_docker else "127.0.0.1"

    try:
        connection = pymysql.connect(
            host=host,
            user="root",         
            password="rootpassword",     
            database="gestion_salas",
            port=3307,            
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
            connect_timeout=5,
            charset="utf8mb4" 
        )
        print(f"Conexión exitosa a la base de datos en host: {host}")
        return connection
    except OperationalError as e:
        print(f"No se pudo conectar a la base de datos: {e}")
        return None
