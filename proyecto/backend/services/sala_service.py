from dao.sala_dao import (
    obtener_salas,
    obtener_sala,
    insertar_sala,
    actualizar_sala,
    eliminar_sala
)

# Listar todas las salas
def service_obtener_salas():
    return obtener_salas()

# Obtener sala
def service_obtener_sala(nombre_sala, edificio):
    return obtener_sala(nombre_sala, edificio)

# Crear sala
def service_crear_sala(data):

    obligatorios = ["nombre_sala", "edificio", "capacidad", "tipo_sala"]
    faltantes = [c for c in obligatorios if c not in data]

    if faltantes:
        return None, f"Faltan campos: {', '.join(faltantes)}", 400
    
    if obtener_sala(data["nombre_sala"], data["edificio"]):
        return None, "Ya existe una sala con ese nombre y edificio", 409

    nueva = insertar_sala(
        data["nombre_sala"],
        data["edificio"],
        data["capacidad"],
        data["tipo_sala"]
    )

    return nueva, None, 201

# Actualizar sala
def service_actualizar_sala(nombre_sala, edificio, data):

    sala = obtener_sala(nombre_sala, edificio)
    if not sala:
        return None, "Sala no encontrada", 404

    actualizada = actualizar_sala(nombre_sala, edificio, data)
    return actualizada, None, 200

# Eliminar sala
def service_eliminar_sala(nombre_sala, edificio):

    sala = obtener_sala(nombre_sala, edificio)
    if not sala:
        return None, "Sala no encontrada", 404

    resultado = eliminar_sala(nombre_sala, edificio)
    return resultado, None, 200
