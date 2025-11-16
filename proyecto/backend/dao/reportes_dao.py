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
                ORDER BY cant_reservas DESC
            """)
            return cursor.fetchall()
        
# Cantidad de reservas y asistencias de profesores y alumnos (grado y posgrado)
def obtener_reservas_asistencias_por_participante():
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
def obtener_reservas_porcentaje_asistencias():
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
        

# Promedio de participantes por sala 
def obtener_promedio_participantes_por_sala():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT r.nombre_sala,
                AVG(sub.cant_participantes) AS promedio_participantes
                FROM reserva r
                JOIN (
                    SELECT rp.id_reserva, COUNT(rp.ci_participante) AS cant_participantes
                    FROM reserva_participante rp
                    GROUP BY rp.id_reserva
                ) AS sub ON r.id_reserva = sub.id_reserva
                GROUP BY r.nombre_sala
            """)
            return cursor.fetchall()
        
'''
def obtener_promedio_participantes_por_sala():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT s.nombre_sala,
                s.capacidad,
                AVG(sub.cant_participantes) AS promedio_participantes,
                (AVG(sub.cant_participantes) / s.capacidad) * 100 AS porcentaje_ocupacion
                FROM sala s
                JOIN reserva r ON s.nombre_sala = r.nombre_sala
                JOIN (
                    SELECT rp.id_reserva, COUNT(rp.ci_participante) AS cant_participantes
                    FROM reserva_participante rp
                    GROUP BY rp.id_reserva
                ) AS sub ON r.id_reserva = sub.id_reserva
                GROUP BY s.nombre_sala, s.capacidad
                ORDER BY promedio_participantes DESC
            """)
            return cursor.fetchall()

'''

# Porcentaje de ocupación de salas por edificio
def obtener_porcentaje_ocupacion_salas_por_edificio():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT s.nombre_sala, s.edificio, s.capacidad,
                ROUND((AVG(sub.cant_participantes) / s.capacidad) * 100, 2) AS porcentaje_ocupacion
                FROM sala s
                JOIN reserva r 
                ON s.nombre_sala = r.nombre_sala AND s.edificio = r.edificio
                JOIN (
                    SELECT rp.id_reserva, COUNT(rp.ci_participante) AS cant_participantes
                    FROM reserva_participante rp
                    GROUP BY rp.id_reserva
                ) AS sub ON r.id_reserva = sub.id_reserva
                GROUP BY s.nombre_sala, s.edificio, s.capacidad
                ORDER BY porcentaje_ocupacion DESC
            """)
            return cursor.fetchall()
        
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
    

# Turnos más demandados (puse top 3 pero se puede cambiar)
def obtener_turnos_mas_demandados():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT t.id_turno,
                    CAST(t.hora_inicio AS CHAR) AS hora_inicio,
                    CAST(t.hora_fin AS CHAR) AS hora_fin,
                    COUNT(r.id_turno) AS cant_reservas
                FROM turno t
                JOIN reserva r ON t.id_turno = r.id_turno
                GROUP BY t.id_turno, t.hora_inicio, t.hora_fin
                ORDER BY cant_reservas DESC
                LIMIT 3
            """)
            return cursor.fetchall()
        

# Cantidad de reservas rechazadas por exceso de personas
def obtener_cantidad_reservas_rechazadas_por_exceso_personas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*) AS reservas_rechazadas_por_exceso
                FROM (
                    SELECT r.id_reserva
                    FROM reserva r
                    JOIN sala s 
                        ON r.nombre_sala = s.nombre_sala 
                       AND r.edificio = s.edificio
                    JOIN reserva_participante rp 
                        ON rp.id_reserva = r.id_reserva
                    GROUP BY r.id_reserva
                    HAVING COUNT(rp.ci_participante) > s.capacidad
                ) AS sub;
            """)
            return cursor.fetchone()

        
# Las 5 personas con más inasistencias
def obtener_5_personas_con_mas_inasistencias():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    rp.ci_participante,
                    p.nombre,
                    p.apellido,
                    COUNT(*) AS cantidad_inasistencias
                FROM reserva_participante rp
                JOIN participante p 
                    ON rp.ci_participante = p.ci
                WHERE rp.asistencia = FALSE
                GROUP BY rp.ci_participante, p.nombre, p.apellido
                ORDER BY cantidad_inasistencias DESC
                LIMIT 5;
            """)
            return cursor.fetchall()


        
# Edificio con mayor cantidad de reservas
def obtener_edificio_mayor_cantidad_reservas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    edificio AS nombre_edificio,
                    COUNT(*) AS total_reservas
                FROM reserva
                GROUP BY edificio
                ORDER BY total_reservas DESC
                LIMIT 1;
            """)
            return cursor.fetchone()

