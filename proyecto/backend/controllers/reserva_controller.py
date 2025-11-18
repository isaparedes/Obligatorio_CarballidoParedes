from flask import Blueprint, jsonify, request
from services.reserva_service import (
    service_obtener_reservas,
    service_obtener_salas_disponibles,
    service_crear_reserva
)

reserva_bp = Blueprint("reservas", __name__)

# GET /reservas
@reserva_bp.get("/")
def get_reservas():
    reservas = service_obtener_reservas()
    return jsonify(reservas), 200

# POST /reservas/salas-disponibles
@reserva_bp.post("/salas-disponibles")
def salas_disponibles_post():
    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()
    fecha = data.get("fecha")  
    cantidad = data.get("cantidad")
    ci_reservante = data.get("ci_reservante")
    lista_participantes = data.get("participantes", [])

    if not fecha or not cantidad or not ci_reservante:
        return jsonify({"error": "Faltan campos obligatorios: fecha, cantidad o ci_reservante"}), 400

    salas, error, status = service_obtener_salas_disponibles(
        fecha, cantidad, ci_reservante, lista_participantes
    )

    if error:
        return jsonify({"error": error}), status

    return jsonify(salas), status

# POST /reservas
@reserva_bp.post("/")
def crear_reserva():
    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()
    nueva, error, status = service_crear_reserva(data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(nueva), status
