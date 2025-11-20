from database.db import get_connection

# Obtener todos los programas académicos
def obtener_programas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM programa_academico")
            return cursor.fetchall()