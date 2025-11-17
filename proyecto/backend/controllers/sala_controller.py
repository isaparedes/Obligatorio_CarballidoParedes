from flask import Blueprint, jsonify, request
from services.sala_service import (service_obtener_salas, service_obtener_sala, service_crear_sala, service_actualizar_sala, service_eliminar_sala)

sala_bp = Blueprint("salas", "salas")

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

    #Validaciones:
    campos_obligatorios = ["nombre_sala", "edificio", "capacidad"]
    faltantes = [c for c in campos_obligatorios if c not in data]
    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    if not isinstance(data["nombre_sala"], str) or len(data["nombre_sala"]) < 1:
        return jsonify({"error": "Nombre de sala inválido"}), 400

    if not isinstance(data["edificio"], str) or len(data["edificio"]) < 1:
        return jsonify({"error": "Edificio inválido"}), 400

    if not isinstance(data["capacidad"], int) or data["capacidad"] <= 0:
        return jsonify({"error": "La capacidad debe ser un entero mayor a 0"}), 400

    if "disponible" in data and not isinstance(data["disponible"], bool):
        return jsonify({"error": "El campo 'disponible' debe ser booleano"}), 400

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


    # Validaciones:
    if "nombre_sala" in data or "edificio" in data:
        return jsonify({"error": "No se pueden modificar los identificadores de la sala"}), 400

    if "capacidad" in data:
        if not isinstance(data["capacidad"], int) or data["capacidad"] <= 0:
            return jsonify({"error": "Capacidad inválida"}), 400

    if "disponible" in data:
        if not isinstance(data["disponible"], bool):
            return jsonify({"error": "El campo 'disponible' debe ser de tipo booleano"}), 400

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
