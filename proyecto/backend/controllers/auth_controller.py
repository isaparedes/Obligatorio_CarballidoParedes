from flask import Blueprint, request, jsonify
from services.auth_service import (
    servicio_registrar_sesion,
    servicio_iniciar_sesion
) 

auth_bp = Blueprint("auth", __name__)

# POST /signup
@auth_bp.post("/signup")
def registrar_sesion():
    data = request.get_json()

    campos_obligatorios = ["ci", "nombre", "apellido", "nombre_programa", "rol", "correo", "contrasena"]
    faltantes = [c for c in campos_obligatorios if c not in data]
    if faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "faltantes": faltantes
        }), 400

    if not isinstance(data["ci"], str) or len(data["ci"]) < 8:
        return jsonify({"error": "Cédula inválida (string, mín. 8 caracteres)"}), 400
    
    if not data["ci"].isdigit():
        return jsonify({"error": "La cédula debe contener solo dígitos numéricos"}), 400

    if not isinstance(data["nombre"], str) or len(data["nombre"]) < 1:
        return jsonify({"error": "Nombre inválido"}), 400

    if not isinstance(data["apellido"], str) or len(data["apellido"]) < 1:
        return jsonify({"error": "Apellido inválido"}), 400
    
    if not isinstance(data["nombre_programa"], str) or len(data["nombre_programa"]) < 1:
        return jsonify({"error": "Programa inválido"}), 400
    
    if not isinstance(data["rol"], str) or (data["rol"]) not in ["alumno", "docente"]:
        return jsonify({"error": "Rol inválido"}), 400
    
    if (not isinstance(data["correo"], str) or 
        ("@ucu.edu.uy" not in data["correo"] and "@correo.ucu.edu.uy" not in data["correo"])):
        return jsonify({"error": "Correo inválido: debe contener @ucu.edu.uy o @correo.ucu.edu.uy"}), 400
    
    if not isinstance(data["contrasena"], str) or len(data["contrasena"]) < 8:
        return jsonify({"error": "Contraseña con mínimo 8 caracteres"}), 400

    usuario, error, status = servicio_registrar_sesion(data)
    if error:
        return jsonify({"error": error}), status
    
    return jsonify({"message": "Usuario registrado", "user": usuario}), 201

# POST /login
@auth_bp.post("/login")
def iniciar_sesion():
    data = request.get_json()

    if (not isinstance(data["correo"], str) or 
        ("@ucu.edu.uy" not in data["correo"] and "@correo.ucu.edu.uy" not in data["correo"])):
        return jsonify({"error": "Correo inválido: debe contener @ucu.edu.uy o @correo.ucu.edu.uy"}), 400
    
    if not isinstance(data["contrasena"], str) or len(data["contrasena"]) < 8:
        return jsonify({"error": "Contraseña inválida"}), 400
    
    token_data, error, status = servicio_iniciar_sesion(data)
    if error:
        return jsonify({"error": error}), status
    
    return jsonify(token_data), 200
