from dao.db import get_connection

# Obtener todas las reservas
def obtener_reservas(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM reserva")
            return cursor.fetchall() 
        
# Insertar nueva reserva
def insertar_reserva(nombre_sala, edificio, fecha, id_turno):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reserva (nombre_sala, edificio, fecha, id_turno, estado)
                VALUES (%s, %s, %s, %s, "activa")
            """, (nombre_sala, edificio, fecha, id_turno))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM reserva
                WHERE nombre_sala = %s AND edificio = %s AND fecha = %s AND id_turno = %s
            """, (nombre_sala, edificio, fecha, id_turno))

            return cursor.fetchone()  
        
# Insertar nueva reserva con participante
def insertar_reserva_participante(ci_participante, id_reserva, fecha_solicitud_reserva):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reserva_participante (ci_participante, id_reserva, fecha_solicitud_reserva, asistencia)
                VALUES (%s, %s, %s, 0)
            """, (ci_participante, id_reserva, fecha_solicitud_reserva))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM reserva_participante
                WHERE ci_participante = %s AND id_reserva = %s
            """, (ci_participante, id_reserva))

            return cursor.fetchone()  

# -------------------------------------------- #

# Obtener la cantidad de reservas que hizo un participante en un mismo día
def obtener_reservas_del_dia(ci, fecha):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT COUNT(r.id_reserva) AS cant_reservas
                FROM reserva r
                JOIN reserva_participante rp
                ON r.id_reserva = rp.id_reserva
                WHERE r.fecha = %s AND rp.ci_participante = %s
            ''', (fecha, ci))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0

# Obtener la cantidad de reservas activas que tiene un participante en una semana determinada
def obtener_reservas_semanales(ci, fecha):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT COUNT(r.id_reserva)
                FROM reserva r
                JOIN reserva_participante rp
                ON r.id_reserva = rp.id_reserva
                WHERE rp.ci_participante = %s
                AND YEARWEEK(r.fecha, 1) = YEARWEEK(%s, 1)
                AND r.estado = "activa"
            ''', (ci, fecha))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else 0
