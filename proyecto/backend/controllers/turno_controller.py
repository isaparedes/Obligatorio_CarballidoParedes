from flask import Blueprint, jsonify
from dao.turno_dao import obtener_turnos, obtener_mas_demandados

turno_bp = Blueprint("turnos", __name__)

# Consulta básica: 

@turno_bp.get("/")
def get_turnos():
    return jsonify(obtener_turnos())


# Consultas obligatorias: 

@turno_bp.get("/mas_demandados")
def get_mas_demandados():
    return jsonify(obtener_mas_demandados())
