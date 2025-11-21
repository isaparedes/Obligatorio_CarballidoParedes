from flask import Blueprint, jsonify
from utils.session import require_auth
from services.edificio_service import service_obtener_edificios

edificio_bp = Blueprint("edificios", __name__)

# GET /edificios
@edificio_bp.get("")
@require_auth
def get_edificios():
    return jsonify(service_obtener_edificios())