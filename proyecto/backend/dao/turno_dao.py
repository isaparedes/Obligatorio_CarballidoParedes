from database.db import get_connection

# Obtener turnos
def obtener_turnos():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM turno")
            return cursor.fetchall()
        

