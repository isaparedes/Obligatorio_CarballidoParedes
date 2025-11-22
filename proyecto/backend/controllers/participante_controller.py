from flask import Blueprint, jsonify, request
from utils.session import require_auth
from services.participante_service import (
    service_obtener_participantes, 
    service_obtener_participante, 
    service_obtener_participante_por_email,
    service_obtener_rol_programa,
    service_crear_participante,
    service_crear_participante_programa,
    service_actualizar_participante, 
    service_eliminar_participante
)

participante_bp = Blueprint("participantes", __name__)

# GET /participantes
@participante_bp.get("/")
@require_auth
def get_participantes():
    return jsonify(service_obtener_participantes())

# GET /participantes/<ci>
@participante_bp.get("/<string:ci>")
@require_auth
def get_participante(ci):
    participante = service_obtener_participante(ci)
    if not participante:
        return jsonify({"error": "Participante no encontrado"}), 404
    return jsonify(participante)

# GET /participantes?email=usuario@correo.ucu.edu.uy
@participante_bp.get("")
@require_auth
def get_participante_por_email():
    email = request.args.get("email")
    if not email:
        return jsonify({"error": "Debe proporcionar un email"}), 400

    participante = service_obtener_participante_por_email(email.strip())
    if not participante:
        return jsonify({"error": "Participante no encontrado"}), 404

    return jsonify(participante)

# GET /participantes/rol-programa/<ci>
@participante_bp.get("/rol-programa/<string:ci>")
@require_auth
def get_rol_participante(ci):
    rol_participante = service_obtener_rol_programa(ci)
    if not rol_participante:
        return jsonify({"error": "Rol no encontrado"}), 404
    return jsonify(rol_participante)

# POST /participantes
@participante_bp.post("/")
@require_auth
def crear_participante():

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()

    campos_obligatorios = ["ci", "nombre", "apellido", "email", "rol", "nombre_programa"]
    faltantes = [c for c in campos_obligatorios if c not in data]
    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    if not isinstance(data["ci"], str) or len(data["ci"]) < 8:
        return jsonify({"error": "Cédula inválida (string, mín. 8 caracteres)"}), 400

    if not isinstance(data["nombre"], str) or len(data["nombre"]) < 1:
        return jsonify({"error": "Nombre inválido"}), 400

    if not isinstance(data["apellido"], str) or len(data["apellido"]) < 1:
        return jsonify({"error": "Apellido inválido"}), 400

    if (not isinstance(data["email"], str) or 
        ("@ucu.edu.uy" not in data["email"] and "@correo.ucu.edu.uy" not in data["email"])):
        return jsonify({"error": "Email inválido: debe contener @ucu.edu.uy o @correo.ucu.edu.uy"}), 400

    if data["rol"] not in ["alumno", "docente"]:
        return jsonify({"error": "Rol inválido: debe ser 'alumno' o 'docente'"}), 400

    if not isinstance(data["nombre_programa"], str) or len(data["nombre_programa"]) < 1:
        return jsonify({"error": "Programa académico inválido"}), 400

    participante, error1, status1 = service_crear_participante(data)
    if error1:
        return jsonify({"error": error1}), status1

    programa, error2, status2 = service_crear_participante_programa(data)
    if error2:
        return jsonify({"error": error2}), status2

    nuevo = {
        "participante": participante,
        "programa": programa
    }

    return jsonify(nuevo), 201


# PUT /participantes/<ci>
@participante_bp.put("/<string:ci>")
@require_auth
def editar_participante(ci):

    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 415

    data = request.get_json()

    if not data:
        return jsonify({"error": "Debes ingresar algún cambio"}), 400

    if "ci" in data:
        return jsonify({"error": "No se puede modificar la CI"}), 400

    if "email" in data and "@ucu.edu.uy" not in data["email"]:
        return jsonify({"error": "Email inválido: debe contener @ucu.edu.uy"}), 400

    if "nombre" in data and (not isinstance(data["nombre"], str) or len(data["nombre"]) < 1):
        return jsonify({"error": "Nombre inválido"}), 400

    if "apellido" in data and (not isinstance(data["apellido"], str) or len(data["apellido"]) < 1):
        return jsonify({"error": "Apellido inválido"}), 400

    actualizado, error, status = service_actualizar_participante(ci, data)

    if error:
        return jsonify({"error": error}), status

    return jsonify(actualizado), status

# DELETE /participantes/<ci>
@participante_bp.delete("/<string:ci>")
@require_auth
def borrar_participante(ci):

    borrado, error, status = service_eliminar_participante(ci)

    if error:
        return jsonify({"error": error}), status

    return jsonify(borrado), status
