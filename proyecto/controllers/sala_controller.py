from flask import Blueprint, jsonify
from dao.sala_dao import obtener_promedio_participantes

sala_bp = Blueprint("salas", __name__)

@sala_bp.get("/promedio_participantes")
def get_promedio_participantes():
    return jsonify(obtener_promedio_participantes())
