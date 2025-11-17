from flask import Blueprint, jsonify
from dao.reportes_dao import (
    obtener_salas_mas_reservadas, 
    obtener_reservas_por_carrera_facultad, 
    obtener_reservas_asistencias_por_participante, 
    obtener_reservas_porcentaje_asistencias,
    obtener_promedio_participantes_por_sala,
    obtener_porcentaje_ocupacion_salas_por_edificio,
    obtener_sanciones_por_participante,
    obtener_turnos_mas_demandados,
    obtener_tres_dias_mas_demandados,
    obtener_cinco_personas_con_mas_inasistencias, 
    obtener_edificio_mayor_cantidad_reservas

)

reportes_bp = Blueprint("reportes", __name__)

# Consultas obligatorias:

@reportes_bp.get("/salas_mas_reservadas")
def get_salas_mas_reservadas():
    return jsonify(obtener_salas_mas_reservadas())

@reportes_bp.get("/reservas_por_carrera_facultad")
def get_reservas_por_carrera_facultad():
    return jsonify(obtener_reservas_por_carrera_facultad())

@reportes_bp.get("/reservas_asistencias_por_participante")
def get_reservas_asistencias_por_participante():
    return jsonify(obtener_reservas_asistencias_por_participante())

@reportes_bp.get("/reservas_porcentaje_asistencias")
def get_reservas_porcentaje_asistencias():
    return jsonify(obtener_reservas_porcentaje_asistencias())

@reportes_bp.get("/promedio_participantes_por_sala")
def get_promedio_participantes_por_sala():
    return jsonify(obtener_promedio_participantes_por_sala())

@reportes_bp.get("/porcentaje_ocupacion_salas_por_edificio")
def get_porcentaje_ocupacion_salas_por_edificio():
    return jsonify(obtener_porcentaje_ocupacion_salas_por_edificio())    

@reportes_bp.get("/sanciones_por_participante")
def get_sanciones_por_participante():
    return jsonify(obtener_sanciones_por_participante())

@reportes_bp.get("/turnos_mas_demandados")
def get_turnos_mas_demandados():
    return jsonify(obtener_turnos_mas_demandados())

# 3 consultas extra 

@reportes_bp.get("/tres_dias_mas_demandados")
def get_tres_dias_mas_demandados():
    return jsonify(obtener_tres_dias_mas_demandados())

@reportes_bp.get("/cinco_personas_con_mas_inasistencias")
def get_cinco_personas_con_mas_inasistencias():
    return jsonify(obtener_cinco_personas_con_mas_inasistencias())

@reportes_bp.get("/edificio_mayor_cantidad_reservas")
def get_edificio_mayor_cantidad_reservas():
    return jsonify(obtener_edificio_mayor_cantidad_reservas())