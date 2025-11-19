from flask import Blueprint, jsonify, request 
from utils.session import require_auth

from services.sancion_service import (
    service_obtener_sanciones, 
    service_obtener_sanciones_participante, 
    service_crear_sancion,
    service_eliminar_sancion
)

sancion_bp = Blueprint("sanciones", __name__)

# GET /sanciones
@sancion_bp.get("/")
# @require_auth
def get_sanciones():
    return jsonify(service_obtener_sanciones())

# GET /sanciones/<ci_participante>
@sancion_bp.get("/<string:ci_participante>")
# @require_auth
def get_sanciones_por_ci(ci_participante):
    sanciones, error, status = service_obtener_sanciones_participante(ci_participante)
    if error:
        return jsonify({"error": error}), status
    if not sanciones:
        return jsonify({"error": "El participante no tiene sanciones"}), 404
    return jsonify(sanciones)

# POST /sanciones
@sancion_bp.post("/")
# @require_auth
def crear_sancion():

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()

    campos_obligatorios = ["ci_participante", "fecha_inicio"]
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

# DELETE /sanciones/<ci_participante>/<fecha_inicio>/<fecha_fin>
@sancion_bp.delete("/<string:ci_participante>/<string:fecha_inicio>/<string:fecha_fin>")
# @require_auth
def eliminar_sancion(ci_participante, fecha_inicio, fecha_fin):

    borrado, error, status = service_eliminar_sancion(ci_participante, fecha_inicio, fecha_fin)

    if error:
        return jsonify({"error": error}), status

    return jsonify(borrado), status
