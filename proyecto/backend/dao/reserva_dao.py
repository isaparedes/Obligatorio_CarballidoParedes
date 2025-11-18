from dao.db import get_connection

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

# Insertar reserva 
def insertar_reserva(nombre_sala, edificio, fecha, id_turno, estado):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reserva (nombre_sala, edificio, fecha, id_turno, estado)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre_sala, edificio, fecha, id_turno, estado))

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
def insertar_reserva_participante(id_reserva, ci):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reserva_participante (id_reserva, ci) 
                VALUES (%s, %s)
            """, (id_reserva, ci))
            conn.commit()
            return {"id_reserva": id_reserva, "ci": ci}

# Eliminar reserva asociada a un participante
def eliminar_reserva_participantes(id_reserva):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                DELETE FROM reserva_participante WHERE id_reserva=%s
            """, (id_reserva,))
            conn.commit()
            return {"deleted": id_reserva}
