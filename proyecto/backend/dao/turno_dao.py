from dao.db import get_connection

# Turnos más demandados (puse top 3 pero se puede cambiar)
def obtener_turnos_mas_demandados():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT t.id_turno,
                    CAST(t.hora_inicio AS CHAR) AS hora_inicio,
                    CAST(t.hora_fin AS CHAR) AS hora_fin,
                    COUNT(r.id_turno) AS cant_reservas
                FROM turno t
                JOIN reserva r ON t.id_turno = r.id_turno
                GROUP BY t.id_turno, t.hora_inicio, t.hora_fin
                ORDER BY cant_reservas DESC
                LIMIT 3;
            """)
            return cursor.fetchall()
        

