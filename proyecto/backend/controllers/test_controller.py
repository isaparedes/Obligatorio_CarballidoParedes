from flask import Blueprint, jsonify
from dao.db import get_connection

test_bp = Blueprint("test", __name__)

@test_bp.get("/db")
def test_db():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 AS conectado")
            return jsonify(cursor.fetchone())
