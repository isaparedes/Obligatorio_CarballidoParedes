from dao.sala_dao import (
    obtener_salas,
    obtener_sala,
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
