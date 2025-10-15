from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
historial_reservas = []

@app.route("/", methods=["GET","POST"])
def home():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form.get("nombre")
        salon = request.form.get("salon")
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")
        reserva = f"Reserva realizada por {nombre} para el salón {salon} el día {fecha} a las {hora}"
        historial_reservas.append(reserva) 

    return render_template("index.html", reservas=historial_reservas)



if __name__ == "__main__":
    app.run(debug=True)

