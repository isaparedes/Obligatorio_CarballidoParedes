from database.db import get_connection

# Obtener todos los participantes
def obtener_participantes():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM participante")
            return cursor.fetchall()

# Obtener participante por CI
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
def insertar_participante(ci, nombre, apellido, email, cursor):
    cursor.execute("""
        INSERT INTO participante (ci, nombre, apellido, email)
        VALUES (%s, %s, %s, %s)
    """, (ci, nombre, apellido, email))
    cursor.execute("""
        SELECT *
        FROM participante
        WHERE ci = %s
    """, (ci,))
    return cursor.fetchone()
        
# Insertar participante con su programa académico
def insertar_participante_programa(ci_participante, nombre_programa, rol, cursor):
    cursor.execute("""
        INSERT INTO participante_programa_academico (ci_participante, nombre_programa, rol)
        VALUES (%s, %s, %s)
    """, (ci_participante, nombre_programa, rol))

    cursor.execute("""
        SELECT *
        FROM participante_programa_academico
        WHERE ci_participante = %s
        AND nombre_programa = %s
    """, (ci_participante, nombre_programa))
    return cursor.fetchone()

# Actualizar participante
def actualizar_participante(ci, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:

            cursor.execute("""
                SELECT nombre, apellido, email
                FROM participante
                WHERE ci = %s
            """, (ci,))
            actual = cursor.fetchone()

            nombre = data.get("nombre", actual["nombre"])
            apellido = data.get("apellido", actual["apellido"])
            email = data.get("email", actual["email"])

            cursor.execute("""
                UPDATE participante
                SET nombre = %s,
                    apellido = %s,
                    email = %s
                WHERE ci = %s
            """, (nombre, apellido, email, ci))

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

            return {"eliminado": ci}

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