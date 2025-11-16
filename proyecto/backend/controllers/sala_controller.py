from flask import Blueprint, jsonify
from dao.sala_dao import  obtener_salas, obtener_promedio_participantes, obtener_porcentaje_ocupacion_por_edificio

sala_bp = Blueprint("salas", __name__)

# Consulta básica:

@sala_bp.get("/")
def get_salas():
    return jsonify(obtener_salas())


# Consultas obligatorias: 

@sala_bp.get("/promedio_participantes")
def get_promedio_participantes():
    return jsonify(obtener_promedio_participantes())

@sala_bp.get("/porcentaje_ocupacion_por_edificio")
def get_porcentaje_ocupacion_por_edificio():
    return jsonify(obtener_porcentaje_ocupacion_por_edificio())    




