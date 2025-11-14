from flask import Flask, render_template
from flask_cors import CORS
from dao.db import get_connection
from controllers.participante_controller import participante_bp
from controllers.reserva_controller import reserva_bp
from controllers.turno_controller import turno_bp
from controllers.sala_controller import sala_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(participante_bp, url_prefix="/participantes")
app.register_blueprint(reserva_bp, url_prefix="/reservas")
app.register_blueprint(turno_bp, url_prefix="/turnos")
app.register_blueprint(sala_bp, url_prefix="/salas")


@app.route("/")
def index():
    conn = get_connection()
    if conn is None:
        return "Error de conexión a la base de datos", 500


    conn.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
