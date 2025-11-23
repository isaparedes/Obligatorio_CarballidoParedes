from flask import Blueprint, jsonify
from utils.session import require_auth

from dao.programa_dao import obtener_programas

programa_bp = Blueprint("programas", __name__)

# GET /programas
@programa_bp.get("/")
# @require_auth
def get_programas():
    return jsonify(obtener_programas())