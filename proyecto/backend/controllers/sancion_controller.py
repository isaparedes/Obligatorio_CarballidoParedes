from flask import Blueprint, jsonify
from dao.sancion_dao import obtener_sanciones

sancion_bp = Blueprint("sanciones", __name__)

# Consulta básica: 

@sancion_bp.get("/")
def get_sanciones():
    return jsonify(obtener_sanciones())







