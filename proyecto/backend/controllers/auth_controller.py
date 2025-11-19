from flask import Blueprint, request, jsonify
from services.auth_service import (
    servicio_registrar_sesion,
    servicio_iniciar_sesion
) 

auth_bp = Blueprint("auth", __name__)

# Agregar alguno de get credenciales

# POST /signup
@auth_bp.post("/signup")
def registrar_sesion():
    data = request.get_json()

    if (not isinstance(data["email"], str) or 
        ("@ucu.edu.uy" not in data["email"] and "@correo.ucu.edu.uy" not in data["email"])):
        return jsonify({"error": "Email inválido: debe contener @ucu.edu.uy o @correo.ucu.edu.uy"}), 400
    
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

    token, error, status = servicio_iniciar_sesion(data)
    if error:
        return jsonify({"error": error}), status
    
    return jsonify({"token": token}), 200
