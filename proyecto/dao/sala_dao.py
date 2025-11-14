from dao.db import get_connection

# Promedio de participantes por sala (con porcentaje)
def obtener_promedio_participantes():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT s.nombre_sala,
                s.capacidad,
                AVG(sub.cant_participantes) AS promedio_participantes,
                (AVG(sub.cant_participantes) / s.capacidad) * 100 AS porcentaje_ocupacion
                FROM sala s
                JOIN reserva r ON s.nombre_sala = r.nombre_sala
                JOIN (
                    SELECT rp.id_reserva, COUNT(rp.ci_participante) AS cant_participantes
                    FROM reserva_participante rp
                    GROUP BY rp.id_reserva
                ) AS sub ON r.id_reserva = sub.id_reserva
                GROUP BY s.nombre_sala, s.capacidad;
            """)
            return cursor.fetchall()

'''
def obtener_promedio_participantes():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT r.nombre_sala,
                AVG(sub.cant_participantes) AS promedio_participantes
                FROM reserva r
                JOIN (
                    SELECT rp.id_reserva, COUNT(rp.ci_participante) AS cant_participantes
                    FROM reserva_participante rp
                    GROUP BY rp.id_reserva
                ) AS sub ON r.id_reserva = sub.id_reserva
                GROUP BY r.nombre_sala
            """)
            return cursor.fetchall()
        
'''
