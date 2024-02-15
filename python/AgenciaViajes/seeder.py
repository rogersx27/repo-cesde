import random

from database_manager import DatabaseManager

entry = input("¿Desea generar datos de ejemplo en la base de datos? (s/n): ")

if entry.lower() != "s":
    exit()

# Creamos una instancia de DatabaseManager con el nombre del archivo de la base de datos
database = r"./db/AgenciaViajes.db"
db_manager = DatabaseManager(database)
destinos = ["Paris", "Roma", "Londres", "Nueva York", "Tokio"]

# Creamos la conexión a la base de datos
db_manager.create_connection()


# Creamos algunas funciones para generar datos aleatorios de destinos y personas
def generar_datos_destino():
    vlr_persona_adulta = round(random.uniform(500, 2000), 2)
    vlr_persona_menor = round(vlr_persona_adulta * random.uniform(0.5, 0.8), 2)
    return (destinos.pop(0), vlr_persona_adulta, vlr_persona_menor)


def generar_datos_persona(id_viaje, vlr_persona_adulta, vlr_persona_menor):
    nombres = ["Juan", "María", "Pedro", "Luisa", "Carlos"]
    apellidos = ["González", "Rodríguez", "Fernández", "López", "Martínez"]
    nro_adultos = random.randint(1, 4)
    nro_ninos = random.randint(0, 3)
    subtotal = round((nro_adultos * vlr_persona_adulta) + (nro_ninos * vlr_persona_menor), 2)
    return (random.choice(nombres), random.choice(apellidos), id_viaje, nro_adultos, nro_ninos, subtotal)

# Seleccionamos todos los destinos para obtener sus IDs nuevamente
existing_destinations = db_manager.select_all_data_destinations()

# Insertamos datos de ejemplo en la tabla Destinos si la tabla está vacía
if existing_destinations.empty:
    for index in range(5):
        datos_destino = generar_datos_destino()

        if db_manager.select_data_destinations_by_name(datos_destino[0]).empty:
            db_manager.insert_data_destinations(datos_destino)
            print("Datos de destinos insertados.")
else:
    print("Ya existen destinos en la base de datos.")

existing_destinations = db_manager.select_all_data_destinations() # Actualizamos la lista de destinos

# Extrañamente se están insertando 11 registros en la tabla Personas.

# Verificamos si hay destinos existentes en la base de datos
if not existing_destinations.empty:
    # Insertamos datos de ejemplo en la tabla Personas, asociados a los destinos
    for index, destino in existing_destinations.iterrows():
        for index in range(random.randint(1, 3)): # <- Esto es lo que está generando 11 registros, pero debería generar entre 1 y 3. No entiendo por qué.
            datos_persona = generar_datos_persona(destino['id'], destino['vlr_personaAdulta'], destino['vlr_personaMenor'])
            print(index)
            db_manager.insert_persona_data(datos_persona)
            print("Datos de personas insertados.")
else:
    print("No hay destinos existentes en la base de datos.")

# Cerramos la conexión a la base de datos
db_manager.close_connection()
