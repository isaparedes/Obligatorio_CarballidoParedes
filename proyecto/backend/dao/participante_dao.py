from dao.db import get_connection

# Obtener participantes
def obtener_participantes():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM participante")
            return cursor.fetchall()

