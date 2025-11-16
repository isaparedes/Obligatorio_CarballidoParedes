from dao.db import get_connection

# Obtener reservas
def obtener_reservas(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM reserva")
            return cursor.fetchall()
        


