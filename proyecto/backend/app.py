from flask import Flask
from flask_cors import CORS
from controllers.participante_controller import participante_bp
from controllers.reserva_controller import reserva_bp
from controllers.turno_controller import turno_bp
from controllers.sala_controller import sala_bp
from controllers.sancion_controller import sancion_bp

app = Flask(__name__)
CORS(app)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(participante_bp, url_prefix="/participantes")
app.register_blueprint(reserva_bp, url_prefix="/reservas")
app.register_blueprint(turno_bp, url_prefix="/turnos")
app.register_blueprint(sala_bp, url_prefix="/salas")
app.register_blueprint(sancion_bp, url_prefix="/sanciones")

@app.route("/")
def index():
    return {"message": "API de gestión de salas funcionando"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
