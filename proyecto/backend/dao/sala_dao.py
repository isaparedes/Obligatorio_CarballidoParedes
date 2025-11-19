from database.db import get_connection

# Obtener todas las salas
def obtener_salas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sala")
            return cursor.fetchall()

# Obtener sala por clave primaria (nombre_sala, edificio)
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

# Insertar sala
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

# Actualizar sala
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

# Obtener salas con cierta capacidad
def obtener_salas_con_capacidad_minima(cantidad):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT nombre_sala, edificio, capacidad, tipo_sala
                FROM sala
                WHERE capacidad >= %s
            ''', (cantidad,))
            return cursor.fetchall()

# Saber si una sala está disponible
def sala_esta_disponible(nombre_sala, edificio, fecha, cant_turnos):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT COUNT(*) AS cant_turnos_reservados
                FROM reserva
                WHERE nombre_sala = %s
                  AND edificio = %s
                  AND fecha = %s
                  AND estado = "activa"
            ''', (nombre_sala, edificio, fecha))

            resultado = cursor.fetchone()

            if not resultado:
                return True

            cantidad = resultado["cant_turnos_reservados"]

            return cantidad < cant_turnos

# Obtener los turnos disponibles que tiene una sala en determinada fecha       
def obtener_turnos_disponibles(nombre_sala, edificio, fecha):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
    
            cursor.execute("SELECT id_turno FROM turnos ORDER BY id_turno")
            todos = [t["id_turno"] for t in cursor.fetchall()]

            cursor.execute("""
                SELECT id_turno
                FROM reserva
                WHERE nombre_sala = %s
                  AND edificio = %s
                  AND fecha = %s
                  AND estado = "activa"
            """, (nombre_sala, edificio, fecha))

            ocupados = {r["id_turno"] for r in cursor.fetchall()}

            disponibles = [t for t in todos if t not in ocupados]

            return disponibles
