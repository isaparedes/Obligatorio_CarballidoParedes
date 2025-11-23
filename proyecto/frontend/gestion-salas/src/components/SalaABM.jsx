import { useState, useEffect } from "react";
import { getEdificios } from "../../api/edificio";
import { getSalas, createSala, deleteSala, editSala } from "../../api/sala";

export default function SalaABM({ salas }) {
  const [mensaje, setMensaje] = useState("");
  const [edificios, setEdificios] = useState([]);
  const [modoEdicion, setModoEdicion] = useState(false);
  const [salasState, setSalasState] = useState(salas);
  const [salaEditando, setSalaEditando] = useState(null);
  const [formData, setFormData] = useState({
    nombre_sala: "",
    capacidad: "",
    tipo_sala: "libre",
    edificio: "",
  });

  useEffect(() => {
    setSalasState(salas);
  }, [salas]);

  const refreshSalas = async () => {
    try {
      const salasObtenidas = await getSalas();
      setSalasState(salasObtenidas);
    } catch (e) {
      console.error("Error refrescando salas", e);
    }
  };

  useEffect(() => {
    const fetchEdificios = async () => {
      try {
        const edificiosObtenidos = await getEdificios();
        setEdificios(edificiosObtenidos);
      } catch (e) {
        console.log("Error obteniendo edificios", e);
      }
    };
    fetchEdificios();
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const resetForm = () => {
    setFormData({
      nombre_sala: "",
      capacidad: "",
      tipo_sala: "libre",
      edificio: "",
    });
    setSalaEditando(null);
    setModoEdicion(false);
  };

  const handleAddSala = async (e) => {
    e.preventDefault();
    if (!formData.capacidad || isNaN(formData.capacidad) || formData.capacidad <= 0) {
      setMensaje("La capacidad debe ser un número entero positivo.");
      return;
    }
    try {
      const dataConCapacidadNumerica = {
        ...formData,
        capacidad: parseInt(formData.capacidad, 10),
      };
      await createSala(dataConCapacidadNumerica);
      setMensaje("Sala creada");
      await refreshSalas(); 
      resetForm();
    } catch (e) {
      setMensaje("Error al crear la sala. Ya existe una sala con dichas credenciales.");
    }
  };

  const handleEditSala = async (e) => {
    e.preventDefault();
    try {
      const dataConCapacidadNumerica = {
        capacidad: parseInt(formData.capacidad, 10),
        tipo_sala: formData.tipo_sala,
      };
      await editSala(formData.nombre_sala, formData.edificio, dataConCapacidadNumerica);
      setMensaje("Sala editada correctamente");
      await refreshSalas(); 
      resetForm();
    } catch (e) {
      setMensaje("Error al editar la sala");
    }
  };

  const handleDeleteSala = async (nombre_sala, edificio) => {
    try {
      const statusCode = await deleteSala(nombre_sala, edificio);
      if (statusCode === 204 || statusCode === 200) {
        setMensaje(`${nombre_sala} del ${edificio} eliminada correctamente.`);
        await refreshSalas(); 
      }
    } catch (e) {
      setMensaje(`Error al eliminar la ${nombre_sala} del ${edificio}. Tiene reservas asociadas.`);
    }
  };

  const seleccionarSalaParaEditar = (s) => {
    setSalaEditando(s);
    setFormData({
      nombre_sala: s.nombre_sala,
      capacidad: s.capacidad,
      tipo_sala: s.tipo_sala,
      edificio: s.edificio,
    });
    setModoEdicion(true);
  };

  return !modoEdicion ? (
    <div className="list-box">
      <h2>Salas</h2>
      {mensaje && <p style={{fontSize: 15}}>{mensaje}</p>}
      <ul className="no-padding">
        {salasState.map((s, i) => (
          <div key={i} className="item-container">
            <li className="item">
              <span>
                {s.nombre_sala} ({s.edificio}) | Capacidad: {s.capacidad} | Tipo: {s.tipo_sala}
              </span>
            </li>
            <div className="button-row">
              <button
                className="small-button small-btn"
                onClick={() => seleccionarSalaParaEditar(s)}
              >
                Editar
              </button>
              <button
                className="small-button small-btn"
                onClick={() => handleDeleteSala(s.nombre_sala, s.edificio)}
              >
                Eliminar
              </button>
            </div>
          </div>
        ))}
      </ul>
      <button className="small-button" onClick={() => setModoEdicion(true)}>
        Agregar sala
      </button>
    </div>
  ) : (
    <div className="list-box">
      <h2>{salaEditando ? "Editar Sala" : "Agregar Sala"}</h2>
      {mensaje && <p style={{fontSize: 15}}>{mensaje}</p>}
      <form onSubmit={salaEditando ? handleEditSala : handleAddSala}>
        <div className="form-group">
          <label htmlFor="nombre_sala">Nombre de la Sala</label>
          <input
            type="text"
            id="nombre_sala"
            name="nombre_sala"
            value={formData.nombre_sala}
            onChange={handleInputChange}
            required
            disabled={!!salaEditando}
          />
        </div>
        <div className="form-group">
          <label htmlFor="capacidad">Capacidad</label>
          <input
            type="number"
            id="capacidad"
            name="capacidad"
            value={formData.capacidad}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="tipo_sala">Tipo de Sala</label>
          <select
            id="tipo_sala"
            name="tipo_sala"
            value={formData.tipo_sala}
            onChange={handleInputChange}
            required
          >
            <option value="libre">Libre</option>
            <option value="posgrado">Posgrado</option>
            <option value="docente">Docente</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="edificio">Edificio</label>
          <select
            id="edificio"
            name="edificio"
            value={formData.edificio}
            onChange={handleInputChange}
            required
            disabled={!!salaEditando}
          >
            <option value="">Seleccione un Edificio</option>
            {edificios.map((edificio, i) => (
              <option key={i} value={edificio.nombre_edificio}>
                {edificio.nombre_edificio}
              </option>
            ))}
          </select>
        </div>
        <button type="submit" className="small-button">
          {salaEditando ? "Guardar cambios" : "Guardar"}
        </button>
        <button type="button" className="small-button" onClick={resetForm}>
          Cancelar
        </button>
      </form>
    </div>
  );
}
