from dao.sala_dao import (
    obtener_salas,
    obtener_sala,
    obtener_turnos_disponibles,
    insertar_sala,
    actualizar_sala,
    eliminar_sala
)

def service_obtener_salas():
    return obtener_salas()

def service_obtener_sala(nombre_sala, edificio):
    return obtener_sala(nombre_sala, edificio)

def service_crear_sala(data):

    if obtener_sala(data["nombre_sala"], data["edificio"]):
        return None, "Ya existe una sala con ese nombre y edificio", 409

    nueva = insertar_sala(
        data["nombre_sala"],
        data["edificio"],
        data["capacidad"],
        data["tipo_sala"]
    )

    return nueva, None, 201

def service_actualizar_sala(nombre_sala, edificio, data):

    sala_actual = obtener_sala(nombre_sala, edificio)
    if not sala_actual:
        return None, "Sala no encontrada", 404

    actualizada = actualizar_sala(nombre_sala, edificio, data)
    return actualizada, None, 200

def service_eliminar_sala(nombre_sala, edificio):

    if not obtener_sala(nombre_sala, edificio):
        return None, "Sala no encontrada", 404

    resultado = eliminar_sala(nombre_sala, edificio)
    return resultado, None, 200

# Obtener turnos disponibles
def service_obtener_turnos_disponibles(nombre_sala, edificio, fecha):

    if not nombre_sala or not isinstance(nombre_sala, str):
        return None, "Nombre de sala inválido", 400

    if not edificio or not isinstance(edificio, str):
        return None, "Edificio inválido", 400

    if not fecha:
        return None, "Debe enviar una fecha", 400

    turnos = obtener_turnos_disponibles(nombre_sala, edificio, fecha)

    if turnos is None:
        return None, "Error al obtener turnos", 500

    if len(turnos) == 0:
        return None, "La sala no tiene turnos disponibles en esa fecha", 404

    return turnos, None, 200