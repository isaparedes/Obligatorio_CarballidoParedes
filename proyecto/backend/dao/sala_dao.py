from dao.db import get_connection

def obtener_salas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sala")
            return cursor.fetchall()

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

def actualizar_sala(nombre_sala, edificio, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:

            cursor.execute("""
                SELECT capacidad, tipo_sala
                FROM sala
                WHERE nombre_sala = %s AND edificio = %s
            """, (nombre_sala, edificio))
            actual = cursor.fetchone()

            capacidad = data.get("capacidad", actual["capacidad"])
            tipo_sala = data.get("tipo_sala", actual["tipo_sala"])

            cursor.execute("""
                UPDATE sala
                SET capacidad = %s,
                    tipo_sala = %s
                WHERE nombre_sala = %s AND edificio = %s
            """, (capacidad, tipo_sala, nombre_sala, edificio))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM sala
                WHERE nombre_sala = %s AND edificio = %s
            """, (nombre_sala, edificio))
            return cursor.fetchone()

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
