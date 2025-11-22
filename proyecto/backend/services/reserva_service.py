import datetime

from dao.reserva_dao import (
    obtener_reservas,
    obtener_reserva,
    obtener_reserva_especifica,
    obtener_reservas_del_dia,
    obtener_reservas_semanales,
    insertar_reserva,
    actualizar_reserva,
    eliminar_reserva,
    insertar_reserva_participante,
    eliminar_reserva_participantes
)

from dao.participante_dao import (
    obtener_participante,
    obtener_rol_programa
)

from dao.sala_dao import (
    obtener_salas_con_capacidad_minima,
    sala_esta_disponible
)

from dao.sancion_dao import obtener_sancionado

from dao.turno_dao import obtener_turnos

# Obtener todas
def service_obtener_reservas():
    return obtener_reservas()

# Obtener por id_reserva
def service_obtener_reserva(id_reserva):
    return obtener_reserva(id_reserva)

# Crear reserva
def service_crear_reserva(data):

    if obtener_reserva_especifica(data["nombre_sala"], data["edificio"], data["fecha"], data["id_turno"]):
        return None, "Ya existe una reserva en esa sala, ese día y ese turno", 409

    nueva = insertar_reserva(
        data["nombre_sala"],
        data["edificio"],
        data["fecha"],
        data["id_turno"]
    )

    for ci in data.get("participantes", []):
        if obtener_participante(ci):
            fecha_solicitud_reserva = datetime.datetime.now()
            insertar_reserva_participante(nueva["id_reserva"], ci, fecha_solicitud_reserva)

    return nueva, None, 201

# Actualizar reserva
def service_actualizar_reserva(id_reserva, data):

    if not obtener_reserva(id_reserva):
        return None, "Reserva no encontrada", 404

    actualizado = actualizar_reserva(id_reserva, data)
    return actualizado, None, 200

# Eliminar reserva
def service_eliminar_reserva(id_reserva):

    if not obtener_reserva(id_reserva):
        return None, "Reserva no encontrada", 404

    eliminar_reserva_participantes(id_reserva)
    eliminar_reserva(id_reserva)

    return {"deleted": id_reserva}, None, 200

# Obtener salas disponibles
def service_obtener_salas_disponibles(fecha, ci_reservante, lista_participantes):

    if (not lista_participantes or lista_participantes[0] == ''):
        lista_participantes = []

    todos = lista_participantes.copy() 
    todos.append(ci_reservante)

    print("fecha:", fecha) # borrar
    print("reservante:", ci_reservante)
    print("participantes:", todos)

    if (len(todos) != len(set(todos))):
        return None, "No puedes repetir participantes", 400
    
    for ci in todos:
        if not obtener_participante(ci):
            return None, f"El participante con cédula {ci} no existe", 404

    
    if obtener_sancionado(ci_reservante):
        print("reservante sancionado") # borrar
        return None, "Quién desea reservar está sancionado", 403
    
    for ci in lista_participantes:
        if obtener_sancionado(ci):
            print(f"participante sancionado: {ci}") # borrar
            return None, f"El participante con la cédula {ci} está sancionado/a", 403

    rol_programa = obtener_rol_programa(ci_reservante)
    if rol_programa:
        rol = rol_programa["rol"]
        programa = rol_programa["tipo"]
    else:
        rol, programa = None, None   

    if not (rol == "docente" or programa == "posgrado"):

        reservas_dia = obtener_reservas_del_dia(ci_reservante, fecha)
        if reservas_dia >= 2:
            return None, "El participante ya tiene 2 horas reservadas ese día", 403
        
        reservas_semana = obtener_reservas_semanales(ci_reservante, fecha)
        if reservas_semana >= 3:
            return None, "El participante ya tiene 3 reservas activas en esa semana", 403


    salas = obtener_salas_con_capacidad_minima(len(todos))
    if not salas:
        return None, "No hay salas que soporten esa cantidad de personas", 404

    if rol == "docente":
        tipos_permitidos = ("libre", "docente", "posgrado")
    elif programa == "posgrado":
        tipos_permitidos = ("libre", "posgrado")
    else:
        tipos_permitidos = ("libre",)

    salas_filtradas = [s for s in salas if s["tipo_sala"] in tipos_permitidos]
    if not salas_filtradas:
        return None, f"No hay salas disponibles", 403

    salas_disponibles = []
    for sala in salas_filtradas:
        nombre_sala, edificio = sala["nombre_sala"], sala["edificio"]
        cant_turnos = len(obtener_turnos())

        if sala_esta_disponible(nombre_sala, edificio, fecha, cant_turnos):
            salas_disponibles.append({
                "nombre_sala": nombre_sala,
                "edificio": edificio,
                "capacidad": sala["capacidad"],
                "tipo_sala": sala["tipo_sala"]
            })

    if not salas_disponibles:
        return None, "No hay salas libres en esa fecha y horario", 404

    return salas_disponibles, None, 200
