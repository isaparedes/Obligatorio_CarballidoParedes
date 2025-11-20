from database.db import get_connection

def get_usuario_por_correo(correo):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM login WHERE correo = %s", (correo,))
            return cursor.fetchone()


def crear_usuario(correo, contrasena_hashed, cursor):
    cursor.execute("""
        INSERT INTO login (correo, contrasena)
        VALUES (%s, %s)
    """, (correo, contrasena_hashed))
    
    cursor.execute("SELECT * FROM login WHERE correo = %s", (correo,))
    return cursor.fetchone()
