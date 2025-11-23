import os
import pymysql
from pymysql.err import OperationalError
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    port = int(os.getenv("DB_PORT"))

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
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
