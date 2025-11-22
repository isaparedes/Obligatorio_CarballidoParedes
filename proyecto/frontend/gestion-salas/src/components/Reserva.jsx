import { useEffect, useState } from "react";
import "./App.css";
import delay from 'delay';
import { getParticipantePorEmail, getParticipantes } from "../../api/participante";
import { getSalasDisponibles } from "../../api/reserva";
import ReservaSala from "./ReservaSala";

export default function Reserva() {
  const [ciReservante, setCiReservante] = useState("");
  const [nombreUsuario, setNombreUsuario] = useState("");
  const [fechaSeleccionada, setFechaSeleccionada] = useState("");
  const [participantesDisponibles, setParticipantesDisponibles] = useState([]);
  const [participantesSeleccionados, setParticipantesSeleccionados] = useState([""]);
  const [error, setError] = useState("");

  const [salasDisp, setSalasDisp] = useState([]);

  const [reserva, setReserva] = useState(false)

  useEffect(() => {
    const email = localStorage.getItem("user");

    getParticipantePorEmail(email)
      .then((usuario) => {
        setCiReservante(usuario.ci);
        setNombreUsuario(usuario.nombre);
      })
      .catch((error) => console.error("Error obteniendo participante:", error));

    getParticipantes()
      .then((participantes) => {
        setParticipantesDisponibles(participantes);
      })
      .catch((error) => console.error("Error obteniendo participantes:", error));
  }, []);

  useEffect(() => {
    if (!ciReservante || participantesDisponibles.length === 0) return;

    setParticipantesDisponibles((prev) =>
      prev.filter((p) => p.ci !== ciReservante && p.ci !== '000000000')
    );
  }, [ciReservante, participantesDisponibles.length]);

  const agregarParticipante = () => {
    if (participantesSeleccionados.length >= 40) return;
    setParticipantesSeleccionados([...participantesSeleccionados, ""]);
  };

  const actualizarParticipante = (index, value) => {
    const nuevos = [...participantesSeleccionados];
    nuevos[index] = value;
    setParticipantesSeleccionados(nuevos);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const datos = {
        fecha: fechaSeleccionada,
        ci_reservante: ciReservante,
        lista_participantes: participantesSeleccionados
      } 
      
      const salas = await getSalasDisponibles(datos);
      setSalasDisp(salas);
      await delay(2000);
      setReserva(true);
    } catch (err) {
      setError(err.message);
    }
  };

    return (
    <div className="inicio">
      {!reserva ? (
        <div id="formulario">
          {error && <p className="error">{error}</p>}

          <h1>Reserva de Sala de Estudio</h1>
          {nombreUsuario && <p>Hola, {nombreUsuario}</p>}

          <form className="datos" onSubmit={handleSubmit}>
            <p className="titulo">
              Elige una fecha
              <input
                type="date"
                required
                value={fechaSeleccionada}
                onChange={(e) => setFechaSeleccionada(e.target.value)}
              />
            </p>

            <p className="titulo">¿Con quién/es quieres reservar?</p>

            {participantesSeleccionados.map((p, i) => (
              <div key={i} style={{ display: "flex", gap: "8px", marginBottom: "8px" }}>
                <select
                  value={p}
                  onChange={(e) => actualizarParticipante(i, e.target.value)}
                  style={{ borderWidth: 1, borderRadius: 8 }}
                >
                  <option value="">Seleccione un participante</option>

                  {participantesDisponibles
                    .filter(
                      (part) => part.ci === p || !participantesSeleccionados.includes(part.ci)
                    )
                    .map((part) => (
                      <option key={part.ci} value={part.ci}>
                        {part.nombre} {part.apellido}{" "}
                        {part.email.includes("@ucu.edu.uy") ? "(docente)" : "(alumno)"}
                      </option>
                    ))}
                </select>

                {i === participantesSeleccionados.length - 1 && (
                  <button type="button" onClick={agregarParticipante}>+</button>
                )}
              </div>
            ))}

            <button type="submit">Enviar</button>
          </form>
        </div>
      ) : (
        <ReservaSala
          fecha={fechaSeleccionada}
          ci_reservante={ciReservante}
          participantes={participantesSeleccionados}
          salas_disponibles={salasDisp} 
        />
      )}
    </div>
  );

}
