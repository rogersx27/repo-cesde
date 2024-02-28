import random
import os

from database_manager import DatabaseManager

# Una función para crear una carpeta "db" para almacenar nuestro archivo .db
db_folder = os.path.join(os.path.dirname(__file__), "db") # C:\Users\PERSONAL\Desktop\Code_Projects\python-delete\cesde-env\python\AgenciaViajes\db
os.makedirs(db_folder, exist_ok=True)

entry = input("¿Deseas generar datos de ejemplo para la base de datos? (s/n): ")

if entry.lower() != "s":
    exit()
    
# Script para generar datos aleatorios #

database = r"python/AgenciaViajes/db/AgenciaViajes.db" # <- Path de la base de datos

destinos = ["París", "Roma", "Londres", "Nueva York", "Tokio"]

min_value = 1000000
max_value = 5000000

# Creamos la instancia
db_manager = DatabaseManager(database)

def generar_datos_destino():
    vlr_adulto = round(random.uniform(min_value, max_value), 2)
    vlr_menor = round(vlr_adulto * random.uniform(0.5, 0.8), 2)
    data = (destinos.pop(0), vlr_adulto, vlr_menor)
    return data

def generar_datos_persona(id_viaje, vlr_adulto, vlr_menor):
    nombres = ["Juan", "María", "Pedro", "Luisa", "Carlos"]
    apellidos = ["López", "Gonzáles", "Rodríguez", "Fernández", "Martínez", "Goméz"]
    nro_adultos = random.randint(1, 5)
    nro_menores = random.randint(0, 4)
    subtotal = round((nro_adultos * vlr_adulto) + (nro_menores * vlr_menor), 2)
    data = (random.choice(nombres), random.choice(apellidos), id_viaje, nro_adultos, nro_menores, subtotal)
    return data
    
destinos_db = db_manager.select_all_data_destinations() # <- Aca hacemos una consulta pero el df está vacío

if destinos_db.empty:
    for _ in range(5):
        datos_destino = generar_datos_destino()    
        db_manager.insert_data_destinations(datos_destino)
        print("Datos de destino insertados")
else:
    print("Datos existentes en la base de datos")
    
destinos_db = db_manager.select_all_data_destinations() # <- Hacemos otra consulta pero el df tiene destinos insertados

for _, destino in destinos_db.iterrows():
    for i in range(random.randint(1, 100)):
        datos_persona = generar_datos_persona(destino['id'], destino['vlr_personaAdulta'], destino['vlr_personaMenor'])
        db_manager.insert_persona_data(datos_persona)
        print(f"Dato de las persona {i} insertados")
        
db_manager.close_connection()




