import { useEffect, useState } from 'react'
import ucuLogo from './assets/ucuLogo.svg'
import './App.css'

function Reserva() {
  const [salas, setSalas] = useState([])

  useEffect(() => {
    fetch("http://localhost:5000/salas")
    .then(res => res.json())
    .then(data => setSalas(data))
  }, [])


  return (
    <div className='inicio'>
      <div id="barraBienvenida">
          <h1> Salas de estudio UCU</h1>
          <img src={ucuLogo}  alt="logo ucu"/> 
      </div>

      <div id="formulario"> 
          <h1>Reserva de Sala de Estudio</h1>
          <form className="datos" method="POST" action="/">
              <p className="titulo">
                Nombre y apellido
                <input type="text" name="nombre" placeholder="Ej: María Pérez" required/>
              </p>
              <p className="titulo">
                {/*Tendría que ser un select con los salones/fecha/hora disponibles*/}
                Salón a reservar
                <input type="text" name="salon" placeholder="Ej: Salon 101" required/>
              </p>
              <p className="titulo">
                <label className="placeholder-label">Fecha</label>
                <input type="date" name="fecha" required/>
              </p>
              <p className="titulo">
                <label className="placeholder-label">Hora</label>
                <input type="time" name="hora" required/>
              </p>
              <button type="submit">Enviar</button>
          </form>
      {salas &&
      <div>
        {salas.map((s, index) => (
          <p key={index}>{s.nombre_sala}, {s.edificio}, {s.capacidad}</p>
        ))}
      </div>
      }
      </div>
    </div>
  )

} 

export default Reserva;
