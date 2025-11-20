import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv  
from controllers.auth_controller import auth_bp
from controllers.reportes_controller import reportes_bp
from controllers.participante_controller import participante_bp
from controllers.reserva_controller import reserva_bp
from controllers.turno_controller import turno_bp
from controllers.sala_controller import sala_bp
from controllers.sancion_controller import sancion_bp
from controllers.programa_controller import programa_bp

load_dotenv()

app = Flask(__name__)
CORS(app)


app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") 

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(participante_bp, url_prefix="/participantes")
app.register_blueprint(reserva_bp, url_prefix="/reservas")
app.register_blueprint(turno_bp, url_prefix="/turnos")
app.register_blueprint(sala_bp, url_prefix="/salas")
app.register_blueprint(sancion_bp, url_prefix="/sanciones")
app.register_blueprint(reportes_bp, url_prefix="/reportes")
app.register_blueprint(programa_bp, url_prefix="/programas")

@app.route("/")
def index():
    return {"message": "API de gestión de salas funcionando"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
