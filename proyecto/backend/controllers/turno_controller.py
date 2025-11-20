from flask import Blueprint, jsonify
from utils.session import require_auth

from dao.turno_dao import obtener_turnos

turno_bp = Blueprint("turnos", __name__)

# GET /turnos
@turno_bp.get("/")
# @require_auth
def get_turnos():
    return jsonify(obtener_turnos())

