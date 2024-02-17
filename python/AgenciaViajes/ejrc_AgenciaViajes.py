from tabulate import tabulate
from time import sleep

import os

from database_manager import DatabaseManager

# Crea una carpeta llamada "db" en la misma ubicación que el archivo de la base de datos
db_folder = os.path.join(os.path.dirname(__file__), "db")
os.makedirs(db_folder, exist_ok=True)

# Inicializar la base de datos
database = r"python/AgenciaViajes/db/AgenciaViajes.db"
db_manager = DatabaseManager(database)


def consult_all_data():
    # Consultar todos los datos
    all_data = db_manager.select_all_data_destinations() # <- Consultar todos los destinos
    destinations = all_data['destino'].values.tolist() # <- Almacenar los destinos en una lista

    # Crear una lista de listas con los datos formateados
    table_allData = [[f"{i + 1}", destination]
                     for i, destination in enumerate(destinations)] # <- Iterar sobre los datos y guardarlos en una lista

    # Imprimir la tabla formateada
    print(tabulate(table_allData, headers=[
          "ID", "Destinos"], tablefmt="pretty"))


def consult_specific_data():
    # Consultar un dato específico
    id = int(
        input("Ingrese el id del dato que desea consultar: "))
    data = db_manager.select_data_destinations(id)  # <- Consultar un dato

    # Crear una lista de listas con los datos formateados
    table_data = [
        [data['destino'].values[0], data['vlr_personaAdulta'].values[0],
            data['vlr_personaMenor'].values[0]]
    ]
    print(tabulate(table_data, headers=["Destino", "Valor persona adulta", "Valor persona menor"],
                   tablefmt="pretty"))


def do_quote():
    # Realizar cotización
    # Pedir todos los datos necesarios para realizar la consulta y posible inserción a la base de datos
    trip_id = int(
        input("Ingrese el id del destino: "))
    adults = int(
        input("Ingrese la cantidad de personas adultas: "))
    children = int(
        input("Ingrese la cantidad de personas menores: "))

    data = db_manager.select_data_destinations(trip_id)  # <- Consultar un dato
    # Crear una lista con los valores de la consulta
    values = [data['vlr_personaAdulta'].values[0],  # <- Almacena el valor de la persona adulta
              data['vlr_personaMenor'].values[0]] # <- Almacena el valor de la persona menor

    total = float((adults * values[0]) + (children * values[1])) # <- Calcular el total

    table_data = [
        [data['destino'].values[0], adults, children, total] # <- Iterar sobre los datos y guardarlos en una lista
    ]

    print(tabulate(table_data, headers=["Destino", "Cantidad de adultos", "Cantidad de menores", "Total"],
                   tablefmt="pretty"))

    # Preguntar si desea guardar la cotización
    save = input("¿Desea guardar la cotización? (s/n): ")
    if save.lower() == "s":
        # Pedimos los datos de la persona que realiza la cotización
        nombre = str(
            input("Ingrese su nombre: "))
        apellido = str(
            input("Ingrese su apellido: "))
        db_manager.insert_persona_data(
            [nombre, apellido, trip_id, adults, children, total]) # <- Insertar los datos de la cotización
        print("Cotización guardada.")
    else:
        print("Cotización no guardada.")


def consult_all_quotes():
    all_quotes = db_manager.select_all_personas_data() # <- Consultar todos los datos de la tabla de cotizaciones
    # Crear una lista de listas con los datos obtenidos de all_quotes
    table_allQuotes = [
        [
            f"{all_quotes['id'].values[i]}",  # <- Almacena el ID
            all_quotes['nombre'].values[i],  # <- Almacena el nombre
            all_quotes['apellido'].values[i],  # <- Almacena el apellido
            all_quotes['id_viaje'].values[i],  # <- Almacena el ID del viaje
            all_quotes['nro_adultos'].values[i], # <- Almacena el número de adultos
            all_quotes['nro_ninos'].values[i], # <- Almacena el número de niños
            all_quotes['subtotal'].values[i]  # <- Almacena el subtotal
        ] for i in range(len(all_quotes)) # <- Iterar sobre los datos y guardarlos en una lista
    ]

    print(tabulate(table_allQuotes, headers=[
        "ID", "Nombre", "Apellido", "ID Viaje", "Nro. adultos", "Nro. niños", "Subtotal"], tablefmt="pretty"))


def consult_specific_quote():
    id_quote = int(
        input("Ingrese el ID de la cotización: "))
    quote = db_manager.select_persona_data(id_quote)  # <- Consultar un dato específico
    trip_id_name = db_manager.select_data_destinations(quote['id_viaje'].values[0].tolist())['destino'].values[0] # <- Consultar un dato específico
    # Crear una lista de listas con los datos formateados de quote
    table_quote = [
        [
            quote['nombre'].values[0],  # <- Almacena el nombre
            quote['apellido'].values[0],  # <- Almacena el apellido
            trip_id_name,  # <- Almacena el nombre del destino
            quote['nro_adultos'].values[0],  # <- Almacena el número de adultos
            quote['nro_ninos'].values[0],  # <- Almacena el número de niños
            quote['subtotal'].values[0]  # <- Almacena el subtotal
        ]
    ]

    print(tabulate(table_quote, headers=[
        "Nombre", "Apellido", "Viaje a", "Nro. adultos", "Nro. niños", "Subtotal"], tablefmt="pretty"))


def add_destination():
    destino = str(input("Ingrese el nombre del destino: "))
    vlr_persona_adulta = float(
        input("Ingrese el valor de la persona adulta: "))
    vlr_persona_menor = float(
        input("Ingrese el valor de la persona menor: "))
    db_manager.insert_data_destinations(
        [destino, vlr_persona_adulta, vlr_persona_menor]) # <- Insertar los datos del destino
    print("Destino añadido.")


def delete_quote():
    id_quote = int(
        input("Ingrese el ID de la cotización que desea eliminar: "))
    db_manager.delete_persona_data(id_quote) # <- Eliminar una cotización
    print("Cotización eliminada.")


def menu():
    while True:
        print("""
        Menú principal
        ----------------------------
        1. Consultar todos los destinos.
        2. Consultar un dato específico.
        3. Realizar cotización.
        4. Panel de administración.
        0. Salir.
        ----------------------------
        """)

        menu = int(input("||==>"))

        if menu == 1:
            consult_all_data() # <- Consultar todos los destinos

        elif menu == 2: 
            consult_specific_data() # <- Consultar un dato específico

        elif menu == 3:
            do_quote() # <- Realizar cotización

        elif menu == 4:
            print("Ingrese la contraseña de administrador: ")
            password = input()
            if password == "admin":
                while True:
                    print("""
                    Panel de administración
                    ----------------------------
                    1. Consultar todas las cotizaciones.
                    2. Consultar una cotización específica.
                    3  Añadir un destino.
                    4. Eliminar una cotización.
                    0. Salir.
                    ----------------------------
                    """)
                    menu_admin = int(input())
                    if menu_admin == 1:
                        consult_all_quotes()  # <- Consultar todos los datos de la tabla de cotizaciones

                    elif menu_admin == 2:
                        consult_specific_data()  # <- Consultar un dato específico

                    elif menu_admin == 3:
                        add_destination()  # <- Añadir un destino

                    elif menu_admin == 4:
                        delete_quote()  # <- Eliminar una cotización

                    elif menu_admin == 0:
                        print("Volviendo al menú principal...")
                        sleep(1)
                        break
        elif menu == 0:
            print("Cerrando programa...")
            db_manager.close_connection()
            sleep(3)
            print("Programa cerrado. ¡Hasta luego!")
            break


if __name__ == "__main__":
    menu()
