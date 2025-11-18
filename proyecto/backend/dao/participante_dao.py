from dao.db import get_connection

# Obtener todos
def obtener_participantes():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM participante")
            return cursor.fetchall()


# Obtener participante por clave primaria (CI)
def obtener_participante(ci):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM participante
                WHERE ci = %s
            """, (ci,))
            return cursor.fetchone()


# Insertar participante
def insertar_participante(ci, nombre, apellido, email):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO participante (ci, nombre, apellido, email)
                VALUES (%s, %s, %s, %s)
            """, (ci, nombre, apellido, email))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM participante
                WHERE ci = %s
            """, (ci,))
            return cursor.fetchone()


# Actualizar participante
def actualizar_participante(ci, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE participante
                SET nombre = %s,
                    apellido = %s,
                    email = %s
                WHERE ci = %s
            """, (
                data.get("nombre"),
                data.get("apellido"),
                data.get("email"),
                ci
            ))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM participante
                WHERE ci = %s
            """, (ci,))
            return cursor.fetchone()


# Eliminar participante
def eliminar_participante(ci):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                DELETE FROM participante
                WHERE ci = %s
            """, (ci,))

            conn.commit()

            return {"deleted": ci}

# ------------------------------------------------ #

# Obtener rol (y programa) por ci
def obtener_rol_programa(ci):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT ppa.rol, pa.tipo
                FROM participante_programa_academico ppa
                JOIN programa_academico pa
                ON ppa.nombre_programa=pa.nombre_programa
                WHERE ppa.ci_participante = %s
            ''', (ci,))
            return cursor.fetchone()    

