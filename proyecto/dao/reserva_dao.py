from dao.db import get_connection

# Salas más reservadas (puse top 3 pero se puede cambiar)
def obtener_salas_mas_reservadas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT nombre_sala, COUNT(*) AS cant_reservas 
                FROM reserva 
                GROUP BY nombre_sala 
                ORDER BY cant_reservas
                DESC LIMIT 3
            """)
            return cursor.fetchall()
        


