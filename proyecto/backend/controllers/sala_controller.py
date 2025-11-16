from flask import Blueprint, jsonify, request
from dao.sala_dao import (obtener_salas, obtener_sala_por_id, insertar_sala, actualizar_sala,eliminar_sala)

sala_bp = Blueprint("salas", __name__)

# Listar todas
@sala_bp.get("/")
def get_salas():
    return jsonify(obtener_salas())

# Obtener una sala
@sala_bp.get("/<int:id_sala>")
def get_sala(id_sala):
    sala = obtener_sala_por_id(id_sala)
    if not sala:
        return jsonify({"error": "Sala no encontrada"}), 404
    return jsonify(sala)

# Crear
@sala_bp.post("/")
def crear_sala():
    data = request.json

    if not data:
        return jsonify({"error": "Faltan datos"}), 400

    nueva = insertar_sala(
        data.get("nombre_sala"),
        data.get("edificio"),
        data.get("capacidad"),
        data.get("tipo_sala")
    )

    return jsonify(nueva), 201

# Actualizar
@sala_bp.put("/<int:id_sala>")
def editar_sala(id_sala):
    data = request.json
    actualizada = actualizar_sala(id_sala, data)
    return jsonify(actualizada)

# Eliminar
@sala_bp.delete("/<int:id_sala>")
def borrar_sala(id_sala):
    resultado = eliminar_sala(id_sala)
    return jsonify(resultado)
