from database.db import get_connection

# Obtener todas las sanciones
def obtener_sanciones(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sancion_participante")
            return cursor.fetchall()

# Obtener sanciones por CI
def obtener_sanciones_participante(ci):
    conn = get_connection()
    with conn: 
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM sancion_participante
                WHERE ci_participante = %s
            """, (ci,))
            return cursor.fetchall()

# Obtener sanción por su clave primaria (ci_participante, fecha_inicio, fecha_fin)
def obtener_sancion(ci_participante, fecha_inicio, fecha_fin):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM sancion_participante
                WHERE ci_participante = %s AND fecha_inicio = %s AND fecha_fin = %s
            """, (ci_participante, fecha_inicio, fecha_fin))
            return cursor.fetchone()

# Insertar sanción
def insertar_sancion(ci_participante, fecha_inicio, fecha_fin):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO sancion_participante (ci_participante, fecha_inicio, fecha_fin)
                VALUES (%s, %s, %s)
            """, (ci_participante, fecha_inicio, fecha_fin))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM sancion_participante
                WHERE ci_participante = %s AND fecha_inicio = %s
            """, (ci_participante, fecha_inicio))
            return cursor.fetchone()

# Eliminar sanción por ID
def eliminar_sancion(ci_participante, fecha_inicio, fecha_fin):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                DELETE FROM sancion_participante
                WHERE ci_participante = %s AND fecha_inicio = %s AND fecha_fin = %s
            """, (ci_participante, fecha_inicio, fecha_fin))

            conn.commit()

            return {"deleted": f"CI: {ci_participante} ({fecha_inicio} - {fecha_fin})"}

# Obtener participante sancionado
def obtener_sancionado(ci):
    conn = get_connection()
    with conn: 
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT *
                FROM sancion_participante
                WHERE ci_participante = %s
                AND fecha_fin > CURDATE()
            ''', (ci,))
            return cursor.fetchone()
