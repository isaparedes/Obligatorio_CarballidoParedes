from flask import Blueprint, jsonify
from dao.sala_dao import  obtener_salas

sala_bp = Blueprint("salas", __name__)

# Consulta básica:

@sala_bp.get("/")
def get_salas():
    return jsonify(obtener_salas())





