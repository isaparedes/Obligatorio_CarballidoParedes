from flask import Blueprint, jsonify
from dao.reserva_dao import obtener_reservas, obtener_salas_mas_reservadas, obtener_reservas_por_carrera_facultad, obtener_asistencias_por_participante, obtener_porcentaje_asistencias

reserva_bp = Blueprint("reservas", __name__)

# Consulta básica:

@reserva_bp.get("/")
def get_reservas():
    return jsonify(obtener_reservas())


# Consultas obligatorias: 

@reserva_bp.get("/salas_mas_reservadas")
def get_salas_mas_reservadas():
    return jsonify(obtener_salas_mas_reservadas())

@reserva_bp.get("/por_carrera_facultad")
def get_reservas_por_carrera_facultad():
    return jsonify(obtener_reservas_por_carrera_facultad())

@reserva_bp.get("/asistencias_por_participante")
def get_asistencias_por_participante():
    return jsonify(obtener_asistencias_por_participante())

@reserva_bp.get("/porcentaje_asistencias")
def get_porcentaje_asistencias():
    return jsonify(obtener_porcentaje_asistencias())