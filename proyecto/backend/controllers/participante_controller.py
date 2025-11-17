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

    # Validaciones
    campos_obligatorios = ["ci", "nombre", "apellido", "edad"]
    faltantes = [c for c in campos_obligatorios if c not in data]
    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    if not isinstance(data["ci"], str) or len(data["ci"]) < 3:
        return jsonify({"error": "CI inválida (debe ser string y mínimo 3 caracteres)"}), 400

    if not isinstance(data["nombre"], str) or len(data["nombre"]) < 1:
        return jsonify({"error": "Nombre inválido"}), 400

    if not isinstance(data["apellido"], str) or len(data["apellido"]) < 1:
        return jsonify({"error": "Apellido inválido"}), 400

    if not isinstance(data["edad"], int) or data["edad"] <= 0:
        return jsonify({"error": "Edad debe ser un entero mayor a 0"}), 400

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

    #Validaciones:
    if "ci" in data:
        return jsonify({"error": "No se puede modificar la CI"}), 400

    if "edad" in data:
        if not isinstance(data["edad"], int) or data["edad"] <= 0:
            return jsonify({"error": "Edad inválida"}), 400

    if "nombre" in data:
        if not isinstance(data["nombre"], str) or len(data["nombre"]) < 1:
            return jsonify({"error": "Nombre inválido"}), 400

    if "apellido" in data:
        if not isinstance(data["apellido"], str) or len(data["apellido"]) < 1:
            return jsonify({"error": "Apellido inválido"}), 400

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
