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

    <div className="metrica-card">
      <h2>Salas Más Reservadas</h2>
      <ul>{salasMasReservadas.map((s, i) => 
        <li key={i}>
          {s.edificio} | {s.nombre_sala} | Cantidad reservas: {s.cant_reservas}
        </li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>Reservas por Carrera y Facultad</h2>
      <ul>{reservasPorCarreraFacultad.map((r, i) => 
        <li key={i}>
          {r.nombre_programa} ({r.nombre}) | Cantidad reservas: {r.cant_reservas}
        </li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>Asistencias por Participante</h2>
      <ul>{asistenciasPorParticipante.map((a, i) => 
        <li key={i}>
          {a.ci} | {a.nombre} {a.apellido} ({a.rol}) | Cantidad reservas: {a.cant_reservas} — Cantidad asistencias: {a.cant_asistencias}
        </li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>Promedio de Participantes por Sala</h2>
      <ul>{promedioParticipantesPorSala.map((p, i) => 
        <li key={i}>{p.nombre_sala}: {p.promedio_participantes}</li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>Porcentaje de Ocupación de Salas por Edificio</h2>
      <ul>{porcentajeOcupacionSalasPorEdificio.map((p, i) => 
        <li key={i}>{p.edificio} : {p.porcentaje_ocupacion}%</li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>Sanciones por Participante</h2>
      <ul>{sancionesPorParticipante.map((s, i) => 
        <li key={i}>{s.ci} | {s.nombre} {s.apellido} | Cantidad sanciones: {s.cant_sanciones}</li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>Turnos Más Demandados</h2>
      <ul>{turnosMasDemandados.map((t, i) => 
        <li key={i}>{t.id_turno} | {t.hora_inicio} - {t.hora_fin} | Cantidad reservas: {t.cant_reservas}</li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>3 Días Más Demandados</h2>
      <ul>{tresDiasMasDemandados.map((d, i) => 
        <li key={i}>{d.dia_semana} | Cantidad reservas: {d.cant_reservas}</li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>5 Personas con Más Inasistencias</h2>
      <ul>{cincoPersonasConMasInasistencias.map((p, i) => 
        <li key={i}>{p.ci_participante} | {p.nombre} {p.apellido} | Cantidad inasistencias: {p.cantidad_inasistencias}</li>
      )}</ul>
    </div>

    <div className="metrica-card">
      <h2>Edificio con Mayor Cantidad de Reservas</h2>
      <p className="li"> {edificioConMasReservas?.nombre_edificio} | Cantidad reservas: {edificioConMasReservas?.total_reservas}</p>
    </div>

  </div>
);
}
