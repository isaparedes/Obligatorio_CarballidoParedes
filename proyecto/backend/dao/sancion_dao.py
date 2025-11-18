from dao.db import get_connection

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

# Obtener sanción por ID
def obtener_sancion_por_id(id_sancion):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM sancion_participante
                WHERE id_sancion = %s
            """, (id_sancion,))
            return cursor.fetchone()

# Insertar sanción
def insertar_sancion(ci, fecha_inicio, fecha_fin):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO sancion_participante (ci_participante, fecha_inicio, fecha_fin)
                VALUES (%s, %s, %s)
            """, (ci, fecha_inicio, fecha_fin))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM sancion_participante
                WHERE ci_participante = %s AND fecha_inicio = %s
            """, (ci, fecha_inicio))
            return cursor.fetchone()

# Actualizar sanción por ID
def actualizar_sancion(id_sancion, data):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE sancion_participante
                SET fecha_inicio = %s,
                    fecha_fin = %s
                WHERE id_sancion = %s
            """, (
                data.get("fecha_inicio"),
                data.get("fecha_fin"),
                id_sancion
            ))

            conn.commit()

            cursor.execute("""
                SELECT *
                FROM sancion_participante
                WHERE id_sancion = %s
            """, (id_sancion,))
            return cursor.fetchone()

# Eliminar sanción por ID
def eliminar_sancion(id_sancion):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                DELETE FROM sancion_participante
                WHERE id_sancion = %s
            """, (id_sancion,))

            conn.commit()

            return {"deleted": id_sancion}
