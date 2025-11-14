from flask import Blueprint, jsonify
from dao.turno_dao import obtener_turnos_mas_demandados

turno_bp = Blueprint("turnos", __name__)

@turno_bp.get("/mas_demandados")
def get_turnos_mas_demandados():
    return jsonify(obtener_turnos_mas_demandados())
