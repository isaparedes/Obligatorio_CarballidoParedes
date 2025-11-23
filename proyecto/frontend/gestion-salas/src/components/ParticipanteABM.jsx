import { useState, useEffect } from "react";
import {
  createParticipante,
  editParticipante,
  deleteParticipante,
  getParticipantes,  
} from "../../api/participante";
import { getProgramas } from "../../api/programa";

export default function ParticipanteABM({ participantes }) {
  const [mensaje, setMensaje] = useState("");
  const [participantesState, setParticipantesState] = useState(participantes);
  const [modoEdicion, setModoEdicion] = useState(false);
  const [participanteEditando, setParticipanteEditando] = useState(null);
  const [programas, setProgramas] = useState([]);

  const [formData, setFormData] = useState({
    ci: "",
    nombre: "",
    apellido: "",
    email: "",
    rol: "alumno",
    nombre_programa: "",
  });

  useEffect(() => {
    setParticipantesState(participantes);
  }, [participantes]);

  useEffect(() => {
    getProgramas()
      .then((programas_academicos) => setProgramas(programas_academicos))
      .catch((err) => console.error("Error al cargar programas académicos:", err));
  }, []);

  const refreshParticipantes = async () => {
    try {
      const participantesObtenidos = await getParticipantes();
      setParticipantesState(participantesObtenidos);
    } catch (e) {
      console.error("Error refrescando participantes", e);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const resetForm = () => {
    setFormData({
      ci: "",
      nombre: "",
      apellido: "",
      email: "",
      rol: "alumno",
      nombre_programa: "",
    });
    setParticipanteEditando(null);
    setModoEdicion(false);
  };

  const handleAddParticipante = async (e) => {
    e.preventDefault();
    try {
      await createParticipante(formData);
      setMensaje("Participante creado exitosamente");
      await refreshParticipantes();
      resetForm();
    } catch (e) {
      setMensaje(e.message || "Error al crear el participante");
    }
  };


  const handleEditParticipante = async (e) => {
    e.preventDefault();
    try {
      await editParticipante(formData.ci, formData);
      setMensaje("Participante editado correctamente");
      await refreshParticipantes(); 
      resetForm();
    } catch (e) {
      setMensaje("Error al editar el participante");
    }
  };

  const handleDeleteParticipante = async (ci) => {
    try {
      const statusCode = await deleteParticipante(ci);
      if (statusCode === 204 || statusCode === 200) {
        setMensaje(`Participante con CI ${ci} eliminado correctamente.`);
        await refreshParticipantes();
      }
    } catch (e) {
      setMensaje(`Error al eliminar el participante con CI ${ci}.`);
    }
  };

  const seleccionarParticipanteParaEditar = (p) => {
    setParticipanteEditando(p);
    setFormData({
      ci: p.ci,
      nombre: p.nombre,
      apellido: p.apellido,
      email: p.email,
      rol: p.rol || "alumno",
      nombre_programa: p.nombre_programa || "",
    });
    setModoEdicion(true);
  };

  return !modoEdicion ? (
    <div className="list-box">
      <h2>Participantes</h2>
      {mensaje && <p style={{fontSize: 15}}>{mensaje}</p>}
      <ul className="no-padding">
        {participantesState
          .filter((p) => p.ci !== "000000000")
          .map((p, i) => (
            <div key={i} className="item-container">
              <li className="item">
                <span>
                  {p.ci} - {p.nombre} {p.apellido} | {p.email}
                </span>
              </li>
              <div className="button-row">
                <button
                  className="small-button small-btn"
                  onClick={() => seleccionarParticipanteParaEditar(p)}
                >
                  Editar
                </button>
                <button
                  className="small-button small-btn"
                  onClick={() => handleDeleteParticipante(p.ci)}
                >
                  Eliminar
                </button>
              </div>
            </div>
          ))}
      </ul>
      <button className="small-button" onClick={() => setModoEdicion(true)}>
        Agregar participante
      </button>
    </div>
  ) : (
    <div className="list-box">
      <h2>{participanteEditando ? "Editar Participante" : "Agregar Participante"}</h2>
      {mensaje && <p style={{fontSize: 15}}>{mensaje}</p>}
      <form onSubmit={participanteEditando ? handleEditParticipante : handleAddParticipante}>
        <div className="form-group">
          <label htmlFor="ci">CI</label>
          <input
            type="text"
            id="ci"
            name="ci"
            value={formData.ci}
            onChange={handleInputChange}
            required
            disabled={!!participanteEditando}
          />
        </div>

        <div className="form-group">
          <label htmlFor="nombre">Nombre</label>
          <input
            type="text"
            id="nombre"
            name="nombre"
            value={formData.nombre}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="apellido">Apellido</label>
          <input
            type="text"
            id="apellido"
            name="apellido"
            value={formData.apellido}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            required
            disabled={!!participanteEditando}
          />
        </div>

        <div className="form-group">
          <label htmlFor="rol">Rol</label>
          <select
            id="rol"
            name="rol"
            value={formData.rol}
            onChange={handleInputChange}
            required
            disabled={!!participanteEditando}
          >
            <option value="alumno">Alumno</option>
            <option value="docente">Docente</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="nombre_programa">Programa Académico</label>
          <select
            id="nombre_programa"
            name="nombre_programa"
            value={formData.nombre_programa}
            onChange={handleInputChange}
            required
          >
            <option value="">Seleccione un programa</option>
            {programas.map((prog, idx) => (
              <option key={idx} value={prog.nombre_programa}>
                {prog.nombre_programa}
              </option>
            ))}
          </select>
        </div>

        <button type="submit" className="small-button">
          {participanteEditando ? "Guardar cambios" : "Guardar"}
        </button>
        <button type="button" className="small-button" onClick={resetForm}>
          Cancelar
        </button>
      </form>
    </div>
  );
}
