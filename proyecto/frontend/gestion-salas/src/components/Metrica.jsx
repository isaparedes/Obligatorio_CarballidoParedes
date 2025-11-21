import { useEffect, useState } from "react";
import "./App.css";
import { 
  getSalasMasReservadas, 
  getReservasPorCarreraFacultad, 
  getAsistenciasPorParticipante, 
  getPorcentajeAsistenciasReservas,
  getPromedioParticipantesPorSala,
  getPorcentajeOcupacionSalasPorEdificio,
  getSancionesPorParticipante,
  getTurnosMasDemandados,
  getTresDiasMasDemandados,
  getCincoPersonasConMasInasistencias,
  getEdificioConMasReservas
} from "../../api/reporte";

export default function Metrica() {
  const [salasMasReservadas, setSalasMasReservadas] = useState([]);
  const [reservasPorCarreraFacultad, setReservasPorCarreraFacultad] = useState([]);
  const [asistenciasPorParticipante, setAsistenciasPorParticipante] = useState([]);
  const [porcentajeAsistenciasReservas, setPorcentajeAsistenciasReservas] = useState([]);
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
          porcentajeAsistencias,
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
          getPorcentajeAsistenciasReservas(),
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
        setPorcentajeAsistenciasReservas(porcentajeAsistencias);
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

      <h2>Top 3 salas más reservadas</h2>
      <ul>{salasMasReservadas.map((s, i) => <li key={i}><strong>{i+1+")"} {s.nombre_sala} ({s.edificio}): </strong>{s.cant_reservas} reserva/s</li>)}</ul>

      <h2>Reservas por carrera y facultad</h2>
      <ul>{reservasPorCarreraFacultad.map((r, i) => <li key={i}><strong>{r.nombre_programa} ({r.nombre}): </strong>{r.cant_reservas} reserva/s</li>)}</ul>

      <h2>Asistencias por participante</h2>
     <ul>
      {asistenciasPorParticipante
        .filter(a => a.ci !== "000000000")
        .map((a, i) => (
          <li key={i}>
            <strong>{a.ci} | {a.nombre} {a.apellido} ({a.rol}):</strong> {a.cant_reservas} reserva/s - {a.cant_asistencias} asistencia/s
          </li>
        ))}
    </ul>

      <h2>Asistencias en reservas</h2>
      <ul>
        <li><strong>Total de reservas: </strong>{porcentajeAsistenciasReservas.total_reservas}</li>
        <li><strong>Reservas utilizadas (por lo menos 1 participante asistió): </strong>{porcentajeAsistenciasReservas.reservas_utilizadas}</li>
        <li><strong>Porcentaje utilizadas:</strong> {porcentajeAsistenciasReservas.porcentaje_utilizadas}%</li>
        <li><strong>Reservas no utilizadas (ninguna asistencia):</strong> {porcentajeAsistenciasReservas.reservas_no_utilizadas}</li>
        <li><strong>Porcentaje no utilizadas:</strong> {porcentajeAsistenciasReservas.porcentaje_no_utilizadas}%</li>
      </ul>

      <h2>Promedio de participantes por sala</h2>
      <ul>{promedioParticipantesPorSala.map((p, i) => <li key={i}><strong>{p.nombre_sala} ({p.edificio}):</strong> {p.promedio_participantes} participantes</li>)}</ul>

      <h2>Porcentaje de ocupación de salas por edificio</h2>
      <ul>{porcentajeOcupacionSalasPorEdificio.map((p, i) => <li key={i}><strong>{p.nombre_sala} ({p.edificio}):</strong> {p.porcentaje_ocupacion}%</li>)}</ul>

      <h2>Sanciones por participante</h2>
      <ul>{sancionesPorParticipante.filter(s => s.ci !== "000000000")
        .map((s, i) => (
          <li key={i}>
            <strong>{s.ci} | {s.nombre} {s.apellido} ({s.rol}):</strong> {s.cant_sanciones} sancion/es
          </li>
        ))}</ul>

      <h2>Top 5 turnos más demandados</h2>
      <ul>{turnosMasDemandados.map((t, i) => <li key={i}><strong>{i+1+")"} {t.hora_inicio} - {t.hora_fin}:</strong> {t.cant_reservas} reserva/s</li>)}</ul>

      <h2>Top 3 días más demandados</h2>
      <ul>{tresDiasMasDemandados.map((d, i) => <li key={i}><strong>{i+1+")"} {d.dia_semana}:</strong> {d.cant_reservas} reserva/s</li>)}</ul>

      <h2>Top 5 personas con más inasistencias</h2>
      <ul>{cincoPersonasConMasInasistencias.map((p, i) => <li key={i}><strong>{i+1+")"} {p.ci_participante} | {p.nombre} {p.apellido} ({p.rol}):</strong> {p.cant_inasistencias} inasistencia/s</li>)}</ul>

      <h2>Edificio con mayor cantidad de reservas</h2>
      <p><strong>{edificioConMasReservas.edificio}:</strong> {edificioConMasReservas.total_reservas} reserva/s</p>
    </div>
  );
}
