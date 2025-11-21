import { useEffect, useState } from "react";
import "./App.css";
import { 
  getSalasMasReservadas, 
  getReservasPorCarreraFacultad, 
  getAsistenciasPorParticipante, 
  getPromedioParticipantesPorSala,
  getPorcentajeOcupacionSalasPorEdificio,
  getSancionesPorParticipante,
  getTurnosMasDemandados,
  getTresDiasMasDemandados,
  getCincoPersonasConMasInasistencias,
  getEdificioConMasReservas
} from "../../api/reportes";

export default function Metrica() {
  const [salasMasReservadas, setSalasMasReservadas] = useState([]);
  const [reservasPorCarreraFacultad, setReservasPorCarreraFacultad] = useState([]);
  const [asistenciasPorParticipante, setAsistenciasPorParticipante] = useState([]);
  const [promedioParticipantesPorSala, setPromedioParticipantesPorSala] = useState([]);
  const [porcentajeOcupacionSalasPorEdificio, setPorcentajeOcupacionSalasPorEdificio] = useState([]);
  const [sancionesPorParticipante, setSancionesPorParticipante] = useState([]);
  const [turnosMasDemandados, setTurnosMasDemandados] = useState([]);
  const [tresDiasMasDemandados, setTresDiasMasDemandados] = useState([]);
  const [cincoPersonasConMasInasistencias, setCincoPersonasConMasInasistencias] = useState([]);
  const [edificioConMasReservas, setEdificioConMasReservas] = useState(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMetricas = async () => {
      try {
        setLoading(true);

        const [
          salas,
          reservasCarrera,
          asistencias,
          promedioSala,
          ocupacionEdificio,
          sanciones,
          turnos,
          dias,
          inasistencias,
          edificio
        ] = await Promise.all([
          getSalasMasReservadas(),
          getReservasPorCarreraFacultad(),
          getAsistenciasPorParticipante(),
          getPromedioParticipantesPorSala(),
          getPorcentajeOcupacionSalasPorEdificio(),
          getSancionesPorParticipante(),
          getTurnosMasDemandados(),
          getTresDiasMasDemandados(),
          getCincoPersonasConMasInasistencias(),
          getEdificioConMasReservas()
        ]);

        setSalasMasReservadas(salas);
        setReservasPorCarreraFacultad(reservasCarrera);
        setAsistenciasPorParticipante(asistencias);
        setPromedioParticipantesPorSala(promedioSala);
        setPorcentajeOcupacionSalasPorEdificio(ocupacionEdificio);
        setSancionesPorParticipante(sanciones);
        setTurnosMasDemandados(turnos);
        setTresDiasMasDemandados(dias);
        setCincoPersonasConMasInasistencias(inasistencias);
        setEdificioConMasReservas(edificio);

      } catch (err) {
        console.error("Error al cargar métricas:", err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchMetricas();
  }, []);

  if (loading) return <div>Cargando métricas...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="inicio">
      <h1>Métricas del Sistema</h1>

      <h2>Salas Más Reservadas</h2>
      <ul>{salasMasReservadas.map((s, i) => <li key={i}>Sala: {s.nombre_sala} - {/*agregar s.edificio en dao */}. Cantidad reservas: {s.cant_reservas}</li>)}</ul>

      <h2>Reservas por Carrera y Facultad</h2>
      <ul>{reservasPorCarreraFacultad.map((r, i) => <li key={i}>{r.nombre_programa} ({r.nombre}). Cantidad reservas: {r.cant_reservas}</li>)}</ul>

      <h2>Asistencias por Participante</h2>
      {/*NO TRAER RESERVAS/ASISTENCIAS ADMIN */}
      <ul>{asistenciasPorParticipante.map((a, i) => <li key={i}>{a.ci} | {a.nombre} {a.apellido} ({a.rol}). Cantidad reservas: {a.cant_reservas}. Asistencias: {a.cant_asistencias}</li>)}</ul>

      <h2>Promedio de Participantes por Sala</h2>
      <ul>{promedioParticipantesPorSala.map((p, i) => <li key={i}>{p.sala}: {p.promedio}</li>)}</ul>

      <h2>Porcentaje de Ocupación de Salas por Edificio</h2>
      <ul>{porcentajeOcupacionSalasPorEdificio.map((p, i) => <li key={i}>{p.edificio}: {p.porcentaje}%</li>)}</ul>

      <h2>Sanciones por Participante</h2>
      <ul>{sancionesPorParticipante.map((s, i) => <li key={i}>{s.participante}: {s.sanciones}</li>)}</ul>

      <h2>Turnos Más Demandados</h2>
      <ul>{turnosMasDemandados.map((t, i) => <li key={i}>{t.turno}: {t.cantidad_reservas}</li>)}</ul>

      <h2>3 Días Más Demandados</h2>
      <ul>{tresDiasMasDemandados.map((d, i) => <li key={i}>{d.dia}: {d.cantidad_reservas}</li>)}</ul>

      <h2>5 Personas con Más Inasistencias</h2>
      <ul>{cincoPersonasConMasInasistencias.map((p, i) => <li key={i}>{p.participante}: {p.inasistencias}</li>)}</ul>

      <h2>Edificio con Mayor Cantidad de Reservas</h2>
      <p>{edificioConMasReservas?.edificio}: {edificioConMasReservas?.cantidad_reservas}</p>
    </div>
  );
}
