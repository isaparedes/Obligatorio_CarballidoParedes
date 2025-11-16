from dao.db import get_connection

# Obtener salas
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

# Obtener sala por id
def obtener_sala_por_id(id_sala):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sala WHERE id_sala = %s", (id_sala,))
            return cursor.fetchone()

# Alta: insertar sala
def insertar_sala(nombre_sala, edificio, capacidad, tipo_sala):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO sala (nombre_sala, edificio, capacidad, tipo_sala)
                VALUES (%s, %s, %s, %s)
                """,
                (nombre_sala, edificio, capacidad, tipo_sala)
            )
            conn.commit()

            nuevo_id = cursor.lastrowid

            cursor.execute("SELECT * FROM sala WHERE id_sala = %s", (nuevo_id,))
            return cursor.fetchone()

# Modificación: actualizar sala
def actualizar_sala(id_sala, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE sala
                SET nombre_sala = %s,
                    edificio = %s,
                    capacidad = %s,
                    tipo_sala = %s
                WHERE id_sala = %s
                """,
                (
                    data.get("nombre_sala"),
                    data.get("edificio"),
                    data.get("capacidad"),
                    data.get("tipo_sala"),
                    id_sala
                )
            )
            conn.commit()

            cursor.execute("SELECT * FROM sala WHERE id_sala = %s", (id_sala,))
            return cursor.fetchone()

# Baja: eliminar sala
def eliminar_sala(id_sala):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM sala WHERE id_sala = %s", (id_sala,))
            conn.commit()
            return {"deleted": id_sala}
