import { useEffect, useState } from "react";
import ucuLogo from "../assets/ucuLogo.svg";
import "../App.css";

export default function Reserva() {
  const [salas, setSalas] = useState([]);
  const [salaSeleccionada, setSalaSeleccionada] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/salas")
      .then(res => res.json())
      .then(data => setSalas(data));
  }, []);

  return (
    <div className="inicio">
      <div id="barraBienvenida">
        <h1>Salas de estudio UCU</h1>
        <img src={ucuLogo} alt="logo ucu" />
      </div>

      <div id="formulario">
        <h1>Reserva de Sala de Estudio</h1>

        <form className="datos">
          {/* Nombre */}
          <p className="titulo">
            Nombre y apellido
            <input type="text" placeholder="Ej: María Pérez" required />
          </p>

          {/* Select de salas */}
          <p className="titulo">
            Salón a reservar  
            <select
              required
              onChange={(e) => {
                const sala = salas.find(s => s.nombre_sala === e.target.value);
                setSalaSeleccionada(sala);
              }}
            >
              <option value="">Seleccione una sala</option>
              {salas.map((s, i) => (
                <option key={i} value={s.nombre_sala}>
                  {s.nombre_sala} — {s.edificio} — Capacidad {s.capacidad}
                </option>
              ))}
            </select>
          </p>

          {/* Select de fechas disponibles SOLO si hay sala seleccionada */}
          {salaSeleccionada && (
            <p className="titulo">
              Fecha disponible
              <select required>
                <option value="">Seleccione una fecha</option>
                {salaSeleccionada.fechas_disponibles?.map((f, i) => (
                  <option key={i} value={f}>{f}</option>
                ))}
              </select>
            </p>
          )}

          <p className="titulo">
            Hora
            <input type="time" required />
          </p>

          {/* Participantes */}
          <p className="titulo">
            Participantes
            <input
              type="number"
              min="1"
              placeholder="Cantidad de personas"
              required
            />
          </p>

          <button type="submit">Enviar</button>
        </form>

        {/* Info de salas */}
        {salas.length > 0 && (
          <div>
            {salas.map((s, i) => (
              <p key={i}>{s.nombre_sala}, {s.edificio}, {s.capacidad}</p>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
