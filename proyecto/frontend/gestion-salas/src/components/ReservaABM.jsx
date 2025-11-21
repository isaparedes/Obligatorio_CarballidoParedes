export default function ReservaABM({reservas}) {

  const handleAddReserva = () => {

  }

  const handleEditReserva = () => {

  }

  const handleDeleteReserva = () => {

  }
  return (
     <div className="list-box">
        <h2>Reservas</h2>
        <ul className="no-padding">
          {reservas.map((r, i) => (
            <div key={i} className="item-container">
              <li className="item">
                <span>
                  N° {r.id_reserva} | {r.nombre_sala} ({r.edificio}) | {/**/}
                  {new Date(r.fecha).toLocaleDateString()} | Turno {r.id_turno} | {r.estado}
                </span>
              </li>

              <div className="button-row">
                <button 
                  className="small-button small-btn"
                  onClick={() => handleEditReserva(r.id_reserva)}
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

        <button className="small-button" onClick={handleAddReserva}>Agregar reserva</button>
      </div>
  )
}