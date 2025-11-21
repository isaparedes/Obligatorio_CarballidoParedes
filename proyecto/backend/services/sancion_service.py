from datetime import datetime
from dateutil.relativedelta import relativedelta

from dao.sancion_dao import (
    obtener_sanciones, 
    obtener_sanciones_participante, 
    insertar_sancion, 
    eliminar_sancion,
    obtener_sancion
)

from dao.participante_dao import obtener_participante

# Obtener todas
def service_obtener_sanciones():
    return obtener_sanciones()

# Obtener sanciones por CI
def service_obtener_sanciones_participante(ci):
    if not obtener_participante(ci):
        return None, "Participante no encontrado", 404
    
    return obtener_sanciones_participante(ci), None, 200

# Crear sanción
def service_crear_sancion(data):

    if not obtener_participante(data["ci_participante"]):
        return None, "Participante no encontrado", 404
    
    fecha_inicio = datetime.fromisoformat(data["fecha_inicio"]) 
    fecha_fin = fecha_inicio + relativedelta(months=2)

    if obtener_sancion(data["ci_participante"], fecha_inicio, fecha_fin):
        return None, "La sanción ya existe", 409

    nueva = insertar_sancion(
        data["ci_participante"],
        fecha_inicio,
        fecha_fin
    )

    return nueva, None, 201

# No se puede actualizar porque los 3 atributos son la PRIMARY KEY preguntar esto

# Eliminar sanción 
def service_eliminar_sancion(ci_participante, fecha_inicio, fecha_fin):

    existente = obtener_sancion(ci_participante, fecha_inicio, fecha_fin)
    if not existente:
        return None, "Sanción no encontrada", 404

    borrado = eliminar_sancion(ci_participante, fecha_inicio, fecha_fin)
    return borrado, None, 200
