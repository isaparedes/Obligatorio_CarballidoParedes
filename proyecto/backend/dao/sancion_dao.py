from dao.db import get_connection

# Obtener sanciones
def obtener_sanciones(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sancion_participante")
            return cursor.fetchall()
        
# --------------------------------------------------- #

# Cantidad de sanciones para profesores y alumnos (grado y posgrado)
def obtener_sanciones_por_participante(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT p.ci, p.nombre, p.apellido, ppa.rol,
                COUNT(sp.ci_participante) AS cant_sanciones
                FROM participante p
                JOIN participante_programa_academico ppa
                ON p.ci = ppa.ci_participante
                LEFT JOIN sancion_participante sp
                ON p.ci = sp.ci_participante
                GROUP BY p.ci, p.nombre, p.apellido, ppa.rol
                ORDER BY cant_sanciones DESC
            ''')
            return cursor.fetchall()
