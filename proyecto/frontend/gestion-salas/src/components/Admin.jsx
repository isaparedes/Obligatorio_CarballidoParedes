import { useEffect, useState } from "react";
import "./App.css";
import { getSalas} from "../../api/sala";
import { getParticipantes} from "../../api/participante";
import { getReservas} from "../../api/reserva";
import { getSanciones} from "../../api/sancion";
import SalaABM from "./SalaABM";
import ParticipanteABM from "./ParticipanteABM";
import ReservaABM from "./ReservaABM";
import SancionABM from "./SancionABM";

export default function Admin() {

  const [salas, setSalas] = useState([]);
  const [participantes, setParticipantes] = useState([]);
  const [reservas, setReservas] = useState([]);
  const [sanciones, setSanciones] = useState([]);

   useEffect(() => {
    const fetchData = async () => {
      const [lista_salas, lista_participantes, lista_reservas, lista_sanciones] =
        await Promise.all([
          getSalas(),
          getParticipantes(),
          getReservas(),
          getSanciones()
        ]);
      setSalas(lista_salas);
      setParticipantes(lista_participantes);
      setReservas(lista_reservas);
      setSanciones(lista_sanciones);
    };

    fetchData();
  }, []);

  return (
    <div className="inicio">
      <h1>Administración</h1>
      <SalaABM salas={salas}/>
      <ParticipanteABM participantes={participantes}/>
      <ReservaABM reservas={reservas}/>
      <SancionABM sanciones={sanciones}/>

    </div>
  );
}
