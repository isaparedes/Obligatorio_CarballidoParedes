from database.db import get_connection

# Obtener todas las reservas
def obtener_reservas():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM reserva")
        return cursor.fetchall()
    
# Obtener reserva por clave primaria (ID)
def obtener_reserva(id_reserva):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM reserva WHERE id_reserva = %s", (id_reserva,))
        return cursor.fetchone()
    
# Obtener reserva por todos sus datos
def obtener_reserva_especifica(nombre_sala, edificio, fecha, id_turno):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM reserva
            WHERE nombre_sala = %s AND edificio = %s AND fecha = %s AND id_turno = %s
        ''', (nombre_sala, edificio, fecha, id_turno))
        return cursor.fetchone()


# Insertar reserva 
def insertar_reserva(nombre_sala, edificio, fecha, id_turno):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reserva (nombre_sala, edificio, fecha, id_turno, estado)
                VALUES (%s, %s, %s, %s, "activa")
            """, (nombre_sala, edificio, fecha, id_turno))

            conn.commit()
            new_id = cursor.lastrowid
            return obtener_reserva(new_id)

# Actualizar reserva
def actualizar_reserva(id_reserva, data):
    conn = get_connection()
    campos = []
    valores = []

    for campo in ["nombre_sala", "edificio", "fecha", "id_turno", "estado"]:
        if campo in data:
            campos.append(f"{campo}=%s")
            valores.append(data[campo])

    if not campos:
        return obtener_reserva(id_reserva)

    valores.append(id_reserva)

    sql = f"UPDATE reserva SET {', '.join(campos)} WHERE id_reserva=%s"

    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, valores)
            conn.commit()
            return obtener_reserva(id_reserva)

# Eliminar reserva 
def eliminar_reserva(id_reserva):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM reserva WHERE id_reserva=%s", (id_reserva,))
            conn.commit()
            return {"deleted": id_reserva}

# Insertar reserva asociada a un participante
def insertar_reserva_participante(id_reserva, ci_participante, fecha_solicitud_reserva):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reserva_participante (id_reserva, ci_participante, fecha_solicitud_reserva, asistencia) 
                VALUES (%s, %s, %s, 0)
            """, (id_reserva, ci_participante, fecha_solicitud_reserva))
            conn.commit()
            return {"id_reserva": id_reserva, "ci_participante": ci_participante}

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
            return resultado["cant_reservas"] if resultado else 0

# Obtener la cantidad de reservas activas que tiene un participante en una semana determinada
def obtener_reservas_semanales(ci, fecha):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT COUNT(r.id_reserva) AS cant_reservas
                FROM reserva r
                JOIN reserva_participante rp
                ON r.id_reserva = rp.id_reserva
                WHERE rp.ci_participante = %s
                AND YEARWEEK(r.fecha, 1) = YEARWEEK(%s, 1)
                AND r.estado = "activa"
            ''', (ci, fecha))
            resultado = cursor.fetchone()
            return resultado["cant_reservas"] if resultado else 0
        

# Obtener la cantidad de reservas activas que tiene un participante en una semana determinada
def obtener_reservas_activas(ci):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT COUNT(r.id_reserva) AS cant_reservas
                FROM reserva r
                JOIN reserva_participante rp
                ON r.id_reserva = rp.id_reserva
                WHERE rp.ci_participante = %s
                AND r.fecha >= CURDATE()
                AND r.estado = "activa"
            ''', (ci))
            resultado = cursor.fetchone()
            return resultado["cant_reservas"] if resultado else 0