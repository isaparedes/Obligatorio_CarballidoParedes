from flask import Blueprint, jsonify, request
from services.participante_service import (service_obtener_participantes, service_obtener_participante, service_crear_participante, service_actualizar_participante, service_eliminar_participante)

participante_bp = Blueprint("participantes", __name__)

# GET /participantes
@participante_bp.get("/")
def get_participantes():
    return jsonify(service_obtener_participantes())


# GET /participantes/<ci>
@participante_bp.get("/<string:ci>")
def get_participante(ci):
    participante = service_obtener_participante(ci)
    if not participante:
        return jsonify({"error": "Participante no encontrado"}), 404
    return jsonify(participante)


# POST /participantes
@participante_bp.post("/")
def crear_participante():

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()
    nuevo, error, status = service_crear_participante(data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(nuevo), status


# PUT /participantes/<ci>
@participante_bp.put("/<string:ci>")
def editar_participante(ci):

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()

    actualizado, error, status = service_actualizar_participante(ci, data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(actualizado), status


# DELETE /participantes/<ci>
@participante_bp.delete("/<string:ci>")
def borrar_participante(ci):

    borrado, error, status = service_eliminar_participante(ci)

    if error:
        return jsonify({"error": error}), status

    return jsonify(borrado), status
