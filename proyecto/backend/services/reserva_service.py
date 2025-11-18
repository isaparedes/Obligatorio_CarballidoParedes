import datetime

from dao.reserva_dao import (
    obtener_reservas, 
    insertar_reserva,
    insertar_reserva_participante,
    obtener_reservas_del_dia,
    obtener_reservas_semanales
)
from dao.sancion_dao import obtener_sancionado
from dao.participante_dao import obtener_rol_programa
from dao.sala_dao import (
    obtener_salas_con_capacidad_minima,
    sala_esta_disponible
)

# Listar todas las reservas
def service_obtener_reservas():
    return obtener_reservas()


# Listar todas las salas disponibles
def service_obtener_salas_disponibles(fecha, cantidad, ci_reservante, lista_participantes):
    
    if obtener_sancionado(ci_reservante):
        return None, "El participante está sancionado", 403
    
    for ci in lista_participantes:
        if obtener_sancionado(ci):
            return None, f"El participante {ci} está sancionado", 403

    rol_programa = obtener_rol_programa(ci_reservante)
    if rol_programa:
        rol, programa = rol_programa
    else:
        rol, programa = None, None   

    if not (rol == "docente" or programa == "posgrado"):

        reservas_dia = obtener_reservas_del_dia(ci_reservante, fecha)
        if reservas_dia >= 2:
            return None, "El participante ya tiene 2 horas reservadas ese día", 403
        
        reservas_semana = obtener_reservas_semanales(ci_reservante, fecha)
        if reservas_semana >= 3:
            return None, "El participante ya tiene 3 reservas activas en esa semana", 403


    salas = obtener_salas_con_capacidad_minima(cantidad)
    if not salas:
        return None, "No hay salas que soporten esa cantidad de personas", 404

    if rol == "docente":
        tipos_permitidos = ("libre", "docente", "posgrado")
    elif programa == "posgrado":
        tipos_permitidos = ("libre", "posgrado")
    else:
        tipos_permitidos = ("libre",)


    salas_filtradas = [s for s in salas if s[3] in tipos_permitidos]
    if not salas_filtradas:
        return None, "No hay salas disponibles según el rol", 403

    salas_disponibles = []
    for sala in salas_filtradas:
        nombre_sala, edificio = sala[0], sala[1]

        if sala_esta_disponible(nombre_sala, edificio, fecha):
            salas_disponibles.append({
                "nombre_sala": nombre_sala,
                "edificio": edificio,
                "capacidad": sala[2],
                "tipo_sala": sala[3]
            })

    if not salas_disponibles:
        return None, "No hay salas libres en esa fecha y horario", 404

    return salas_disponibles, None, 200


# Crear reserva
def service_crear_reserva(data):

    obligatorios = ["nombre_sala", "edificio", "fecha", "id_turno", "ci_participantes"]
    faltantes = [c for c in obligatorios if c not in data]
    if faltantes:
        return None, f"Faltan campos: {', '.join(faltantes)}", 400

    nueva = insertar_reserva(
        data["nombre_sala"],
        data["edificio"],
        data["fecha"],
        data["id_turno"]
    )

    for ci in data["ci_participantes"]:
        insertar_reserva_participante(
            ci,
            nueva[0],  
            datetime.datetime.now()
        )

    return {
        "id_reserva": nueva[0],
        "nombre_sala": nueva[1],
        "edificio": nueva[2],
        "fecha": nueva[3],
        "id_turno": nueva[4],
        "estado": nueva[5]
    }, None, 201
