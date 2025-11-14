from flask import Blueprint, jsonify
from dao.reserva_dao import obtener_salas_mas_reservadas, obtener_reservas_por_carrera_facultad, obtener_reservas

reserva_bp = Blueprint("reservas", __name__)

@reserva_bp.get("/salas_mas_reservadas")
def get_salas_mas_reservadas():
    return jsonify(obtener_salas_mas_reservadas())

@reserva_bp.get("/por_carrera_facultad")
def get_reservas_por_carrera_facultad():
    return jsonify(obtener_reservas_por_carrera_facultad())

@reserva_bp.get("/")
def get_reservas():
    return jsonify(obtener_reservas())