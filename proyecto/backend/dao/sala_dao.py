from dao.db import get_connection

# Obtener salas
def obtener_salas():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sala")
            return cursor.fetchall()

# Obtener salas disponibles
def obtener_salas_disponibles(fecha_inicio, fecha_fin, cantidad):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT s.nombre_sala, s.edificio, s.capacidad
                FROM sala s
                WHERE s.capacidad >= %s
                AND NOT EXISTS (
                    SELECT 1 
                    FROM reserva r
                    WHERE r.nombre_sala = s.nombre_sala
                      AND r.edificio = s.edificio
                      AND (
                          (%s BETWEEN r.fecha_inicio AND r.fecha_fin) OR
                          (%s BETWEEN r.fecha_inicio AND r.fecha_fin) OR
                          (r.fecha_inicio BETWEEN %s AND %s)
                      )
                );
            """, (cantidad, fecha_inicio, fecha_fin, fecha_inicio, fecha_fin))
            return cursor.fetchall()
