from dao.db import get_connection

# Obtener todas las salas
def obtener_salas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sala")
            return cursor.fetchall()


# Obtener salas disponibles
def obtener_salas_disponibles(fecha_inicio, fecha_fin, cantidad):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT s.nombre_sala, s.edificio, s.capacidad
                FROM sala s
                WHERE s.capacidad >= %s
                AND NOT EXISTS (
                    SELECT 1 
                    FROM reserva r
                    WHERE r.nombre_sala = s.nombre_sala
                      AND r.edificio = s.edificio
                      AND (
                          (%s BETWEEN r.fecha_inicio AND r.fecha_fin) OR
                          (%s BETWEEN r.fecha_inicio AND r.fecha_fin) OR
                          (r.fecha_inicio BETWEEN %s AND %s)
                      )
                );
            """, (cantidad, fecha_inicio, fecha_fin, fecha_inicio, fecha_fin))
            return cursor.fetchall()


# Obtener sala por clave primaria (nombre_sala + edificio)
def obtener_sala(nombre_sala, edificio):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM sala
                WHERE nombre_sala = %s AND edificio = %s
            """, (nombre_sala, edificio))
            return cursor.fetchone()


# Insertar nueva sala
def insertar_sala(nombre_sala, edificio, capacidad, tipo_sala):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO sala (nombre_sala, edificio, capacidad, tipo_sala)
                VALUES (%s, %s, %s, %s)
            """, (nombre_sala, edificio, capacidad, tipo_sala))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM sala
                WHERE nombre_sala = %s AND edificio = %s
            """, (nombre_sala, edificio))

            return cursor.fetchone()


# Actualizar sala (clave primaria no cambia)
def actualizar_sala(nombre_sala, edificio, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE sala
                SET capacidad = %s,
                    tipo_sala = %s
                WHERE nombre_sala = %s AND edificio = %s
            """, (
                data.get("capacidad"),
                data.get("tipo_sala"),
                nombre_sala,
                edificio
            ))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM sala
                WHERE nombre_sala = %s AND edificio = %s
            """, (nombre_sala, edificio))

            return cursor.fetchone()


# Eliminar sala
def eliminar_sala(nombre_sala, edificio):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                DELETE FROM sala
                WHERE nombre_sala = %s AND edificio = %s
            """, (nombre_sala, edificio))

            conn.commit()

            return {"deleted": f"{nombre_sala} - {edificio}"}
