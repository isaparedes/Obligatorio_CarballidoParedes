from flask import Blueprint, request, jsonify
from utils.session import require_auth

from services.reserva_service import (
    service_obtener_reservas,
    service_obtener_reserva,
    service_obtener_salas_disponibles,
    service_crear_reserva,
    service_actualizar_reserva,
    service_eliminar_reserva
)

from datetime import datetime

reserva_bp = Blueprint("reservas", __name__)

# GET /reservas
@reserva_bp.get("/")
@require_auth
def get_reservas():
    return jsonify(service_obtener_reservas())

# GET /reservas/<id>
@reserva_bp.get("/<int:id_reserva>")
@require_auth
def get_reserva(id_reserva):
    reserva = service_obtener_reserva(id_reserva)
    if not reserva:
        return jsonify({"error": "Reserva no encontrada"}), 404
    return jsonify(reserva)

# POST /reservas
@reserva_bp.post("/")
@require_auth
def crear_reserva():

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()

    campos = ["nombre_sala", "edificio", "fecha", "id_turno", "participantes"]
    faltantes = [c for c in campos if c not in data]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    try:
        datetime.strptime(data["fecha"], "%Y-%m-%d")
    except:
        return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

    if not isinstance(data["id_turno"], int):
        return jsonify({"error": "id_turno debe ser entero"}), 400

    nueva, error, status = service_crear_reserva(data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(nueva), status

# PUT /reservas/<id>
@reserva_bp.put("/<int:id_reserva>")
@require_auth
def editar_reserva(id_reserva):

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes ingresar algún cambio"}), 400

    if "id_reserva" in data:
        return jsonify({"error": "No se puede modificar el id_reserva"}), 400

    if "fecha" in data:
        try:
            datetime.strptime(data["fecha"], "%Y-%m-%d")
        except:
            return jsonify({"error": "Formato de fecha inválido"}), 400

    if "id_turno" in data and not isinstance(data["id_turno"], int):
        return jsonify({"error": "id_turno debe ser entero"}), 400

    if "estado" in data:
        if data["estado"] not in ["activa", "finalizada", "cancelada"]:
            return jsonify({"error": "Estado inválido"}), 400

    actualizado, error, status = service_actualizar_reserva(id_reserva, data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(actualizado), status

# DELETE /reservas/<id> 
@reserva_bp.delete("/<int:id_reserva>")
@require_auth
def borrar_reserva(id_reserva):

    borrado, error, status = service_eliminar_reserva(id_reserva)

    if error:
        return jsonify({"error": error}), status

    return jsonify(borrado), status

# POST /reservas/salas/disponibles
@reserva_bp.post("/salas/disponibles")
@require_auth
def get_salas_disponibles():
    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()
    fecha = data.get("fecha")  
    ci_reservante = data.get("ci_reservante")
    lista_participantes = data.get("lista_participantes", [])

    if not fecha or not ci_reservante:
        return jsonify({"error": "Faltan campos obligatorios: fecha o ci_reservante"}), 400

    salas, error, status = service_obtener_salas_disponibles(
        fecha, ci_reservante, lista_participantes
    )

    if error:
        return jsonify({"error": error}), status

    return jsonify(salas), status