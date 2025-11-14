from dao.db import get_connection


# Extra: ver lo de los tildes
def obtener_participantes():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM participante")
            return cursor.fetchall()
