from flask import Blueprint, jsonify
from dao.sancion_dao import obtener_sanciones, obtener_sanciones_por_participante

sancion_bp = Blueprint("sanciones", __name__)

# Consulta básica: 

@sancion_bp.get("/")
def get_sanciones():
    return jsonify(obtener_sanciones())


# Consultas obligatorias: 

@sancion_bp.get("/por_participante")
def get_sanciones_por_participante():
    return jsonify(obtener_sanciones_por_participante())





