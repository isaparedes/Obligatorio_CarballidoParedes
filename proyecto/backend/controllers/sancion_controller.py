from flask import Blueprint, jsonify, request 
from services.sancion_service import (
    service_obtener_sanciones, 
    service_obtener_sanciones_participante, 
    service_crear_sancion,
    service_actualizar_sancion, 
    service_eliminar_sancion
)

sancion_bp = Blueprint("sanciones", __name__)

# GET /sanciones
@sancion_bp.get("/")
def get_sanciones():
    return jsonify(service_obtener_sanciones())

# GET /sanciones/<ci_participante>
@sancion_bp.get("/<string:ci_participante>")
def get_sanciones_por_ci(ci_participante):
    sanciones = service_obtener_sanciones_participante(ci_participante)
    if not sanciones:
        return jsonify({"error": "El usuario no tiene sanciones"}), 404
    return jsonify(sanciones)

# POST /sanciones
@sancion_bp.post("/")
def crear_sancion():

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()

    campos_obligatorios = ["ci_participante", "fecha_inicio", "fecha_fin"]
    faltantes = [c for c in campos_obligatorios if c not in data]

    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    if not isinstance(data["ci_participante"], str) or len(data["ci_participante"]) < 8:
        return jsonify({"error": "CI inválida"}), 400

    nuevo, error, status = service_crear_sancion(data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(nuevo), status

# PUT /sanciones/<ci_participante>
@sancion_bp.put("/<string:ci_participante>")
def editar_sancion(ci_participante):

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()

    if "ci_participante" in data:
        return jsonify({"error": "No se puede modificar la CI del participante"}), 400
    
    actualizado, error, status = service_actualizar_sancion(ci_participante, data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(actualizado), status

# DELETE /sanciones/<ci_participante>
@sancion_bp.delete("/<string:ci_participante>")
def eliminar_sancion(ci_participante):

    borrado, error, status = service_eliminar_sancion(ci_participante)

    if error:
        return jsonify({"error": error}), status

    return jsonify(borrado), status
