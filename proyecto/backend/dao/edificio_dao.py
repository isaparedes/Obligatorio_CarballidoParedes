from database.db import get_connection

# Obtener todos los edificios
def obtener_edificios():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM edificio")
            return cursor.fetchall()