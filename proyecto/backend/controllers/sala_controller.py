from flask import Blueprint, jsonify, request
from services.sala_service import (
    service_obtener_salas,
    service_obtener_sala,
    service_obtener_turnos_disponibles,
    service_crear_sala,
    service_actualizar_sala,
    service_eliminar_sala
)

sala_bp = Blueprint("salas", __name__)

# GET /salas
@sala_bp.get("/")
def get_salas():
    return jsonify(service_obtener_salas())

# GET /salas/<nombre_sala>/<edificio>
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
    
    obligatorios = ["nombre_sala", "edificio", "capacidad", "tipo_sala"]
    faltantes = [c for c in obligatorios if c not in data]

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
        return jsonify({"error": "Capacidad debe ser un entero positivo"}), 400
    
    if not isinstance(data["tipo_sala"], str) or data["tipo_sala"] not in ["posgrado", "docente", "libre"]:
        return jsonify({"error": "Tipo de sala inválido"}), 400

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

    if not data:
        return jsonify({"error": "Debes ingresar algún cambio"}), 400
    
    if "nombre_sala" in data or "edificio" in data:
        return jsonify({"error": "No se puede modificar el nombre de la sala o el edificio"}), 400

    if "capacidad" in data:
        if not isinstance(data["capacidad"], int) or data["capacidad"] <= 0:
            return jsonify({"error": "Capacidad debe ser un entero positivo"}), 400

    if "tipo_sala" in data:
        if not isinstance(data["tipo_sala"], str) or data["tipo_sala"] not in ["posgrado", "docente", "libre"]:
            return jsonify({"error": "Tipo de sala inválido"}), 400

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

# GET /salas/turnos/disponibles
@sala_bp.get("/turnos/disponibles")
def obtener_turnos_disponibles_controller():
    nombre_sala = request.args.get("nombre_sala")
    edificio = request.args.get("edificio")
    fecha = request.args.get("fecha")

    turnos, error, status = service_obtener_turnos_disponibles(nombre_sala, edificio, fecha)

    if error:
        return jsonify({"error": error}), status

    return jsonify({"turnos_disponibles": turnos}), status