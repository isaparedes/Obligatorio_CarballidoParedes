import delay from 'delay';
import { getTurnosDisponiblesSegunSala } from '../../api/sala';
import { useState } from 'react';
import { createReserva } from '../../api/reserva';


export default function ReservaSala({ fecha, ci_reservante, participantes, salas_disponibles, setReserva }) {

    const [sala, setSala] = useState("");
    const [turnos, setTurnos] = useState(null);

    const [mensaje, setMensaje] = useState("")

    const handleObtenerTurnos = async (sala) => {
        try {
            setSala(sala);
            const turnos_sala = await getTurnosDisponiblesSegunSala(sala.nombre_sala, sala.edificio, fecha);
            setTurnos(turnos_sala);
            console.log(turnos_sala)
        }
        catch (e) {
            console.log(`Error al obtener turnos de ${sala.nombre_sala} - ${sala.edificio}`)
        }
    }

    const handleReservar = async (turno) => {
        try {
            const todos = [ci_reservante, ...participantes];
            const datos = {
                nombre_sala: sala.nombre_sala,
                edificio: sala.edificio,
                fecha: fecha,
                id_turno: turno.id_turno,
                participantes: todos
            } 
            const reserva = await createReserva(datos);
            setMensaje("Reserva creada correctamente")
            await delay(2000)
            setMensaje("");
            setReserva(false);
            // ver que hacemos
        }
        catch (e) {
            setMensaje("Error al reservar")
            console.log('Error al reservar')
        }
    }

    return (
        <div>
            {mensaje != "" && <p style={{fontSize: 15}}>{mensaje}</p>}
            {!turnos ? (
            <>
                <h2>Elija una sala disponible</h2>
                {salas_disponibles && salas_disponibles.length > 0 ? (
                <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
                    {salas_disponibles.map((s, i) => (
                    <button key={i} style={{ width: 250 }} onClick={() => handleObtenerTurnos(s)}>
                        <strong>{s.nombre_sala} — {s.edificio}</strong> (Capacidad: {s.capacidad})
                    </button>
                    ))}
                </div>
                ) : (
                <p>No hay salas disponibles.</p>
                )}
            </>
            ) : (
            <>
                <h2>Turnos disponibles</h2>
                {turnos.length > 0 ? (
                <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
                    {turnos.map((t, i) => (
                    <button key={i} style={{ width: 200 }} onClick={() => handleReservar(t)}>
                        {t.hora_inicio} — {t.hora_fin}
                    </button>
                    ))}
                </div>
                ) : (
                <p>No hay turnos disponibles.</p>
                )}
            </>
            )}
        </div>
    );


}
