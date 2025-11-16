from flask import Blueprint, jsonify
from dao.turno_dao import obtener_turnos

turno_bp = Blueprint("turnos", __name__)

# Consulta básica: 

@turno_bp.get("/")
def get_turnos():
    return jsonify(obtener_turnos())

