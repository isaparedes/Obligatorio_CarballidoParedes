import os
import pymysql
from pymysql.err import OperationalError
from dotenv import load_dotenv

load_dotenv(override=True)

def get_connection():
    host = os.environ.get("DB_HOST")
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    database = os.environ.get("DB_NAME")
    port = int(os.environ.get("DB_PORT"))

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
