from dao.db import get_connection

# Obtener sanciones
def obtener_sanciones(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sancion_participante")
            return cursor.fetchall()
        
# Obtener participante sancionado
def obtener_sancionado(ci):
    conn = get_connection()
    with conn: 
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT *
                FROM sanciones
                WHERE ci_participante = %s
                AND fecha_fin > CURDATE()
            ''', (ci,))
            return cursor.fetchone()
        
