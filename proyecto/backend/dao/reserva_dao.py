from dao.db import get_connection

# Salas más reservadas (puse top 3 pero se puede cambiar)
def obtener_salas_mas_reservadas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT nombre_sala, COUNT(*) AS cant_reservas 
                FROM reserva 
                GROUP BY nombre_sala 
                ORDER BY cant_reservas
                DESC LIMIT 3
            """)
            return cursor.fetchall()
        
# Cantidad de reservas por carrera y facultad
def obtener_reservas_por_carrera_facultad(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT pa.nombre_programa, f.nombre, COUNT(r.id_reserva) AS cant_reservas
                FROM reserva r
                JOIN reserva_participante rp 
                ON r.id_reserva=rp.id_reserva
                JOIN participante_programa_academico ppa
                ON rp.ci_participante=ppa.ci_participante
                JOIN programa_academico pa
                ON ppa.nombre_programa=pa.nombre_programa
                JOIN facultad f
                ON pa.id_facultad=f.id_facultad
                GROUP BY pa.nombre_programa, f.nombre
            """)
            return cursor.fetchall()
        
# Cantidad de reservas y asistencias de profesores y alumnos (grado y posgrado)
#...

# Extra
def obtener_reservas(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM reserva")
            return cursor.fetchall()


