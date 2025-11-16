from dao.db import get_connection

# Obtener sanciones
def obtener_sanciones(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sancion_participante")
            return cursor.fetchall()
        
