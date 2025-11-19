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
