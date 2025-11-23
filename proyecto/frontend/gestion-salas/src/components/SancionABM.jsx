import { useState, useEffect } from "react";
import { getSanciones, createSancion, deleteSancion } from "../../api/sancion";

export default function SancionABM({ sanciones }) {
  const [mensaje, setMensaje] = useState("");
  const [sancionesState, setSancionesState] = useState(sanciones);
  const [modoEdicion, setModoEdicion] = useState(false);
  const [formData, setFormData] = useState({
    ci_participante: "",
    fecha_inicio: "",
  });

  useEffect(() => {
    setSancionesState(sanciones);
  }, [sanciones]);

  const formatDate = (date) => {
    const d = new Date(date);
    return d.toISOString().split("T")[0]; 
  };

  const refreshSanciones = async () => {
    try {
      const sancionesObtenidas = await getSanciones();
      setSancionesState(sancionesObtenidas);
    } catch (e) {
      console.error("Error refrescando sanciones", e);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const resetForm = () => {
    setFormData({
      ci_participante: "",
      fecha_inicio: "",
    });
    setModoEdicion(false);
  };

  const handleAddSancion = async (e) => {
    e.preventDefault();
    try {
      await createSancion({
        ci_participante: formData.ci_participante,
        fecha_inicio: new Date(formData.fecha_inicio),
      });
      setMensaje("Sanción creada exitosamente");
      await refreshSanciones(); 
      resetForm();
    } catch (e) {
      setMensaje("Error al crear la sanción");
    }
  };

  const handleDeleteSancion = async (ci_participante, fecha_inicio, fecha_fin) => {
    try {
      const statusCode = await deleteSancion(
        ci_participante,
        formatDate(fecha_inicio),
        formatDate(fecha_fin)
      );
      if (statusCode === 204 || statusCode === 200) {
        setMensaje(`Sanción de CI ${ci_participante} eliminada correctamente.`);
        await refreshSanciones(); 
      }
    } catch (e) {
      setMensaje(`Error al eliminar la sanción de CI ${ci_participante}.`);
    }
  };

  return !modoEdicion ? (
    <div className="list-box">
      <h2>Sanciones</h2>
      {mensaje && <p style={{fontSize: 15}}>{mensaje}</p>}
      <ul className="no-padding">
        {sancionesState
          .filter((s) => s.ci_participante !== "000000000")
          .map((s, i) => (
            <div key={i} className="item-container">
              <li className="item">
                <span>
                  CI {s.ci_participante} |{" "}
                  {new Date(s.fecha_inicio).toLocaleDateString()} -{" "}
                  {new Date(s.fecha_fin).toLocaleDateString()}
                </span>
              </li>
              <div className="button-row">
                <button
                  className="small-button small-btn"
                  onClick={() =>
                    handleDeleteSancion(
                      s.ci_participante,
                      s.fecha_inicio,
                      s.fecha_fin
                    )
                  }
                >
                  Eliminar
                </button>
              </div>
            </div>
          ))}
      </ul>
      <button className="small-button" onClick={() => setModoEdicion(true)}>
        Agregar sanción
      </button>
    </div>
  ) : (
    <div className="list-box">
      <h2>Agregar Sanción</h2>
      {mensaje && <p style={{fontSize: 15}}>{mensaje}</p>}
      <form onSubmit={handleAddSancion}>
        <div className="form-group">
          <label htmlFor="ci_participante">CI Participante</label>
          <input
            type="text"
            id="ci_participante"
            name="ci_participante"
            value={formData.ci_participante}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="fecha_inicio">Fecha Inicio</label>
          <input
            type="date"
            id="fecha_inicio"
            name="fecha_inicio"
            value={formData.fecha_inicio}
            onChange={handleInputChange}
            required
          />
        </div>

        <button type="submit" className="small-button">
          Guardar
        </button>
        <button type="button" className="small-button" onClick={resetForm}>
          Cancelar
        </button>
      </form>
    </div>
  );
}
