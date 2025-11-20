// GET /reportes/salas_mas_reservadas
const getSalasMasReservadas = async (accessToken) => {
  const url = "http://localhost:5000/reportes/salas_mas_reservadas";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Salas más reservadas obtenidas:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener las salas más reservadas: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/reservas_por_carrera_facultad
const getReservasPorCarreraFacultad = async (accessToken) => {
  const url = "http://localhost:5000/reportes/reservas_por_carrera_facultad";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Reservas por carrera y facultad obtenidas:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener las reservas por carrera y facultad: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/reservas_asistencias_por_participante
const getAsistenciasPorParticipante = async (accessToken) => {
  const url = "http://localhost:5000/reportes/reservas_asistencias_por_participante";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Asistencias por participante obtenidas:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener las asistencias por participante: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/promedio_participantes_por_sala
const getPromedioParticipantesPorSala = async (accessToken) => {
  const url = "http://localhost:5000/reportes/promedio_participantes_por_sala";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Promedios de participantes por sala obtenidos:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener los promedios de participantes por sala: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/porcentaje_ocupacion_salas_por_edificio
const getPorcentajeOcupacionSalasPorEdificio = async (accessToken) => {
  const url = "http://localhost:5000/reportes/porcentaje_ocupacion_salas_por_edificio";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Porcentajes de ocupación de salas por edificio obtenidos:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener los porcentajes de ocupación de salas por edificio: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/sanciones_por_participante
const getSancionesPorParticipante = async (accessToken) => {
  const url = "http://localhost:5000/reportes/sanciones_por_participante";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Sanciones por participante obtenidas:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener las sanciones por participante: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/turnos_mas_demandados
const getTurnosMasDemandados = async (accessToken) => {
  const url = "http://localhost:5000/reportes/turnos_mas_demandados";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Turnos más demandados obtenidos:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener los turnos más demandados: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/tres_dias_mas_demandados
const getTresDiasMasDemandados = async (accessToken) => {
  const url = "http://localhost:5000/reportes/tres_dias_mas_demandados";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Días más demandados obtenidos:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener los días más demandados: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/cinco_personas_con_mas_inasistencias
const getCincoPersonasConMasInasistencias = async (accessToken) => {
  const url = "http://localhost:5000/reportes/cinco_personas_con_mas_inasistencias";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Personas con más inasistencias obtenidas:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener las personas con más inasistencias: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reportes/edificio_mayor_cantidad_reservas
const getEdificioConMasReservas = async (accessToken) => {
  const url = "http://localhost:5000/reportes/edificio_mayor_cantidad_reservas";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Edificio con mayor cantidad de reservas obtenido:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener el edificio con mayor cantidad de reservas: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};