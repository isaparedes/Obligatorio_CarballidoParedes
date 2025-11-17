# sala_controller.py

from flask import Blueprint, jsonify, request
from services.sala_service import (
    service_obtener_salas,
    service_obtener_sala,
    service_crear_sala,
    service_actualizar_sala,
    service_eliminar_sala
)

sala_bp = Blueprint("salas", __name__)

# GET /salas
@sala_bp.get("/")
def get_salas():
    return jsonify(service_obtener_salas())


# GET /salas/<nombre>/<edificio>
@sala_bp.get("/<string:nombre_sala>/<string:edificio>")
def get_sala(nombre_sala, edificio):
    sala = service_obtener_sala(nombre_sala, edificio)
    if not sala:
        return jsonify({"error": "Sala no encontrada"}), 404
    return jsonify(sala)


# POST /salas
@sala_bp.post("/")
def crear_sala():

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()
    nueva, error, status = service_crear_sala(data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(nueva), status


# PUT /salas/<nombre>/<edificio>
@sala_bp.put("/<string:nombre_sala>/<string:edificio>")
def editar_sala(nombre_sala, edificio):

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()
    actualizada, error, status = service_actualizar_sala(nombre_sala, edificio, data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(actualizada), status


# DELETE /salas/<nombre>/<edificio>
@sala_bp.delete("/<string:nombre_sala>/<string:edificio>")
def borrar_sala(nombre_sala, edificio):

    resultado, error, status = service_eliminar_sala(nombre_sala, edificio)

    if error:
        return jsonify({"error": error}), status

    return jsonify(resultado), status
