import { useState, useEffect } from "react";
import {
  getReservas,
  createReserva,
  editReserva,
  deleteReserva,
  getSalasDisponibles
} from "../../api/reserva";
import { getParticipantes } from "../../api/participante";
import { getTurnosDisponiblesSegunSala } from "../../api/sala";

export default function ReservasABM() {
  // Listado y feedback
  const [reservas, setReservas] = useState([]);
  const [mensaje, setMensaje] = useState("");
  const [error, setError] = useState("");

  // Alta con restricciones (flujo tipo Reserva.jsx para admin)
  const [participantesDisponibles, setParticipantesDisponibles] = useState([]);
  const [participantesSeleccionados, setParticipantesSeleccionados] = useState([""]); // el primero será el reservante
  const [fechaSeleccionada, setFechaSeleccionada] = useState("");
  const [salasDisp, setSalasDisp] = useState([]);
  const [salaSeleccionada, setSalaSeleccionada] = useState(null);
  const [turnosDisp, setTurnosDisp] = useState([]);

  // Edición
  const [reservaEditando, setReservaEditando] = useState(null);
  const [formData, setFormData] = useState({
    fecha: "",
    id_turno: "",
    estado: "activa"
  });

  // Cargar reservas y participantes
  useEffect(() => {
    getReservas()
      .then((data) => setReservas(data))
      .catch((err) => setError(err.message));

    getParticipantes()
      .then((data) => setParticipantesDisponibles(data.filter(p => p.ci !== "000000000")))
      .catch((err) => setError(err.message));
  }, []);

  // Helpers
  const agregarParticipante = () => {
    setParticipantesSeleccionados((prev) => [...prev, ""]);
  };

  const actualizarParticipante = (index, value) => {
    const nuevos = [...participantesSeleccionados];
    nuevos[index] = value;
    setParticipantesSeleccionados(nuevos);
  };

  const resetFlujoAlta = () => {
    setParticipantesSeleccionados([""]);
    setFechaSeleccionada("");
    setSalasDisp([]);
    setSalaSeleccionada(null);
    setTurnosDisp([]);
    setMensaje("");
    setError("");
  };

  const resetEdicion = () => {
    setReservaEditando(null);
    setFormData({ fecha: "", id_turno: "", estado: "activa" });
  };

  // Consultar salas disponibles (con reglas; el primero es reservante)
  const handleConsultarSalas = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const reservante = participantesSeleccionados[0];
      const invitados = participantesSeleccionados.slice(1);
      const datos = {
        fecha: fechaSeleccionada,
        ci_reservante: reservante,
        lista_participantes: invitados
      };
      const salas = await getSalasDisponibles(datos);
      setSalasDisp(salas);
      setMensaje("Salas disponibles cargadas.");
    } catch (err) {
      setError(err.message || "Error consultando salas disponibles.");
      setSalasDisp([]);
    }
  };

  // Elegir sala y cargar turnos
  const handleElegirSala = async (sala) => {
    setSalaSeleccionada(sala);
    setTurnosDisp([]);
    setMensaje("");
    setError("");
    try {
      const turnos = await getTurnosDisponiblesSegunSala(
        sala.nombre_sala,
        sala.edificio,
        fechaSeleccionada
      );
      setTurnosDisp(turnos);
      setMensaje("Turnos disponibles cargados.");
    } catch {
      setError("Error al obtener turnos de la sala seleccionada.");
    }
  };
  // Crear reserva (POST /reservas)
  const handleCrearReserva = async (turno) => {
    try {
      const todos = participantesSeleccionados;
      const datos = {
        nombre_sala: salaSeleccionada.nombre_sala,
        edificio: salaSeleccionada.edificio,
        fecha: fechaSeleccionada,
        id_turno: turno.id_turno,
        participantes: todos
      };
      const nueva = await createReserva(datos);
      setReservas((prev) => [...prev, nueva]);
      resetFlujoAlta();
      setMensaje("Reserva creada exitosamente");
    } catch (err) {
      setError(err.message);
    }
  };

  // Editar reserva (PUT /reservas/:id)
  const handleEditReserva = async (e) => {
  e.preventDefault();
  try {
    const body = { estado: formData.estado }; // 👈 solo enviamos estado
    const editada = await editReserva(reservaEditando.id_reserva, body);
    setReservas((prev) =>
      prev.map((r) => (r.id_reserva === reservaEditando.id_reserva ? editada : r))
    );
    resetEdicion();
    setMensaje("Reserva editada correctamente");
  } catch (err) {
    setError(err.message);
  }
};


  // Eliminar reserva (DELETE /reservas/:id)
  const handleDeleteReserva = async (id) => {
    try {
      const status = await deleteReserva(id);
      if (status === 204) {
        setReservas((prev) => prev.filter((r) => r.id_reserva !== id));
        setMensaje(`Reserva ${id} eliminada correctamente`);
      }
    } catch (err) {
      setError(err.message);
    }
  };

  const seleccionarReservaParaEditar = (r) => {
    setReservaEditando(r);
    setFormData({
      estado: r.estado
    });
  };

  return (
    <div className="list-box">
      <h2>Reservas</h2>
      {/* Listado de reservas */}
      <ul className="no-padding">
        {reservas.map((r, i) => (
          <div key={i} className="item-container">
            <li className="item">
              <span>
                N° {r.id_reserva} | {r.nombre_sala} ({r.edificio}) |{" "}
                {new Date(r.fecha).toLocaleDateString()} | Turno {r.id_turno} | {r.estado}
              </span>
            </li>
            <div className="button-row">
              <button
                className="small-button small-btn"
                onClick={() => seleccionarReservaParaEditar(r)}
              >
                Editar
              </button>
              <button
                className="small-button small-btn"
                onClick={() => handleDeleteReserva(r.id_reserva)}
              >
                Eliminar
              </button>
            </div>
          </div>
        ))}
      </ul>
      {mensaje && <p>{mensaje}</p>}
      {error && <p className="error">{error}</p>}
      {/* Alta de reserva */}
      {!reservaEditando && (
        <>
          <h3>Agregar Reserva</h3>
          <form onSubmit={handleConsultarSalas}>
            <input
              type="date"
              value={fechaSeleccionada}
              onChange={(e) => setFechaSeleccionada(e.target.value)}
              required
            />
            <p>Seleccionar participantes (el primero será el reservante)</p>
            {participantesSeleccionados.map((p, i) => (
              <div key={i}>
                <select value={p} onChange={(e) => actualizarParticipante(i, e.target.value)}>
                  <option value="">Seleccione un participante</option>
                  {participantesDisponibles.map((part) => (
                    <option key={part.ci} value={part.ci}>
                      {part.nombre} {part.apellido}
                    </option>
                  ))}
                </select>
                {i === participantesSeleccionados.length - 1 && (
                  <button type="button" onClick={agregarParticipante}>+</button>
                )}
              </div>
            ))}
            <button type="submit">Consultar salas</button>
          </form>

          {salasDisp.length > 0 && !salaSeleccionada && (
            <div>
              <h3>Salas disponibles</h3>
              {salasDisp.map((s, i) => (
                <button key={i} onClick={() => handleElegirSala(s)}>
                  {s.nombre_sala} — {s.edificio} (Capacidad: {s.capacidad})
                </button>
              ))}
            </div>
          )}

          {salaSeleccionada && turnosDisp.length > 0 && (
            <div>
              <h3>Turnos disponibles</h3>
              {turnosDisp.map((t, i) => (
                <button key={i} onClick={() => handleCrearReserva(t)}>
                  {t.hora_inicio} — {t.hora_fin}
                </button>
              ))}
            </div>
          )}
        </>
      )}

      {/* Edición de reserva */}
      {reservaEditando && (
        <form onSubmit={handleEditReserva}>
          <h3>Editar Reserva N° {reservaEditando.id_reserva}</h3>
          <select
            name="estado"
            value={formData.estado}
            onChange={(e) => setFormData({ ...formData, estado: e.target.value })}
          >
            <option value="activa">Activa</option>
            <option value="cancelada">Cancelada</option>
            <option value="finalizada">Finalizada</option>
          </select>
          <button type="submit">Guardar cambios</button>
          <button type="button" onClick={resetEdicion}>Cancelar</button>
        </form>
      )}
    </div>
  );
}
