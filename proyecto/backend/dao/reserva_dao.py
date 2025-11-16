from dao.db import get_connection

# Obtener participantes
def obtener_reservas(): 
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM reserva")
            return cursor.fetchall()
        
# --------------------------------------------------- #

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
                ORDER BY cant_reservas DESC
            """)
            return cursor.fetchall()
        
# Cantidad de reservas y asistencias de profesores y alumnos (grado y posgrado)
def obtener_asistencias_por_participante():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor: 
            cursor.execute('''
                SELECT p.ci, p.nombre, p.apellido, ppa.rol,
                COUNT(rp.id_reserva) AS cant_reservas,
                SUM(rp.asistencia = 1) AS cant_asistencias
                FROM participante p
                JOIN participante_programa_academico ppa 
                ON p.ci = ppa.ci_participante
                LEFT JOIN reserva_participante rp 
                ON p.ci = rp.ci_participante
                GROUP BY p.ci, p.nombre, p.apellido, ppa.rol
                ORDER BY cant_reservas DESC;
            ''')
            return cursor.fetchall()


# Porcentaje de reservas efectivamente utilizadas vs. canceladas/no asistidas
def obtener_porcentaje_asistencias():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT SUM(CASE WHEN r.estado = 'finalizada' 
                AND EXISTS (
                    SELECT 1 
                    FROM reserva_participante rp 
                    WHERE rp.id_reserva = r.id_reserva
                    AND rp.asistencia = TRUE
                )
                THEN 1 ELSE 0 END) AS reservas_utilizadas,
                SUM(CASE WHEN r.estado <> 'finalizada' OR 
                NOT EXISTS (
                    SELECT 1 
                    FROM reserva_participante rp 
                    WHERE rp.id_reserva = r.id_reserva
                    AND rp.asistencia = TRUE
                )
                THEN 1 ELSE 0 END) AS reservas_no_utilizadas,
                COUNT(*) AS total_reservas,
                ROUND(SUM(CASE WHEN r.estado = 'finalizada'
                AND EXISTS (
                    SELECT 1 
                    FROM reserva_participante rp 
                    WHERE rp.id_reserva = r.id_reserva
                    AND rp.asistencia = TRUE
                )
                THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS porcentaje_utilizadas,
                ROUND(SUM(CASE WHEN r.estado <> 'finalizada' OR
                NOT EXISTS (
                    SELECT 1 
                    FROM reserva_participante rp 
                    WHERE rp.id_reserva = r.id_reserva
                    AND rp.asistencia = TRUE
                )
                THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS porcentaje_no_utilizadas
                FROM reserva r;
            ''')
            return cursor.fetchall()
        

