from flask import Blueprint, jsonify
from dao.reserva_dao import obtener_salas_mas_reservadas

reserva_bp = Blueprint("reservas", __name__)

@reserva_bp.get("/salas_mas_reservadas")
def get_salas_mas_reservadas():
    return jsonify(obtener_salas_mas_reservadas())
