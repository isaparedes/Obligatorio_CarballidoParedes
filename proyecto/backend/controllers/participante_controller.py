from flask import Blueprint, jsonify
from dao.participante_dao import obtener_participantes

participante_bp = Blueprint("participantes", __name__)

# Consulta básica:

@participante_bp.get("/")
def get_participantes():
    return jsonify(obtener_participantes())
