from flask import Blueprint, jsonify, request
from dao.reserva_dao import obtener_reservas
from dao import sala_dao

reserva_bp = Blueprint("reservas", __name__)

# Consulta básica:

@reserva_bp.get("/")
def get_reservas():
    return jsonify(obtener_reservas())

@reserva_bp.route('/salas/disponibles', methods=['GET'])
def salas_disponibles():
    fecha_inicio = request.args.get("fecha_inicio")
    fecha_fin = request.args.get("fecha_fin")
    cantidad = int(request.args.get("cantidad"))

    salas = sala_dao.obtener_salas_disponibles(fecha_inicio, fecha_fin, cantidad)
    return jsonify(salas)

