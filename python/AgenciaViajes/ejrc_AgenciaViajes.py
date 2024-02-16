from tabulate import tabulate
from time import sleep

from database_manager import DatabaseManager

# Inicializar la base de datos
database = r"./db/AgenciaViajes.db"
db_manager = DatabaseManager(database)


def consult_all_data():
    # Consultar todos los datos
    all_data = db_manager.select_all_data_destinations()
    destinations = all_data['destino'].values.tolist()  # <- Obtener todos los destinos y guardarlos en una lista

    # Crear una lista de listas con los datos formateados
    table_allData = [[f"{i + 1}", destination] for i, destination in enumerate(destinations)]

    # Imprimir la tabla formateada
    print(tabulate(table_allData, headers=["ID", "Destinos"], tablefmt="pretty"))


def consult_specific_data():
    # Consultar un dato específico
    id = int(input("Ingrese el id del dato que desea consultar: "))
    data = db_manager.select_data_destinations(id)  # <- Consultar un dato

    # Crear una lista de listas con los datos formateados
    table_data = [
        [data['destino'].values[0], data['vlr_personaAdulta'].values[0], data['vlr_personaMenor'].values[0]]
    ]
    print(tabulate(table_data, headers=["Destino", "Valor persona adulta", "Valor persona menor"],
                   tablefmt="pretty"))


def do_quote():
    # Realizar cotización
    # Pedir todos los datos necesarios para realizar la consulta y posible inserción a la base de datos
    trip_id = int(input("Ingrese el id del destino: "))
    adults = int(input("Ingrese la cantidad de personas adultas: "))
    children = int(input("Ingrese la cantidad de personas menores: "))

    data = db_manager.select_data_destinations(trip_id)  # <- Consultar un dato
    values = [data['vlr_personaAdulta'].values[0], data['vlr_personaMenor'].values[0]]  # <- Guardamos los precios

    total = float((adults * values[0]) + (children * values[1]))  # <- Calculamos el total

    table_data = [
        [data['destino'].values[0], adults, children, total]
    ]

    print(tabulate(table_data, headers=["Destino", "Cantidad de adultos", "Cantidad de menores", "Total"],
                   tablefmt="pretty"))

    # Preguntar si desea guardar la cotización
    save = input("¿Desea guardar la cotización? (s/n): ")
    if save.lower() == "s":
        # Pedimos los datos de la persona que realiza la cotización
        nombre = str(input("Ingrese su nombre: "))
        apellido = str(input("Ingrese su apellido: "))

        db_manager.insert_persona_data([nombre, apellido, trip_id, adults, children, total])  # <- Guardar la cotización
        print("Cotización guardada.")
    else:
        print("Cotización no guardada.")


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

        menu = int(input())

        if menu == 1:
            consult_all_data()

        elif menu == 2:
            consult_specific_data()

        elif menu == 3:
            do_quote()

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
                    3. Eliminar una cotización.
                    0. Salir.
                    ----------------------------
                    """)
                    menu_admin = int(input())
                    if menu_admin == 1:
                        all_quotes = db_manager.select_all_personas_data()
                        table_allQuotes = [[f"{all_quotes['id'].values[i]}", all_quotes['nombre'].values[i], all_quotes['apellido'].values[i], all_quotes['id_viaje'].values[i], all_quotes['nro_adultos'].values[i], all_quotes['nro_ninos'].values[i], all_quotes['subtotal'].values[i]] for i in range(len(all_quotes))] #<- refactorizar
                        print(tabulate(table_allQuotes, headers=["ID", "Nombre", "Apellido", "ID Viaje", "Nro. adultos", "Nro. niños", "Subtotal"], tablefmt="pretty"))
                    elif menu_admin == 2:
                        id_quote = int(input("Ingrese el ID de la cotización: "))
                        quote = db_manager.select_persona_data(id_quote)
                        # trip = db_manager.select_data_destinations(quote['id_viaje'].values[0].tolist())
                        trip_id_name = (db_manager.select_data_destinations(quote['id_viaje'].values[0].tolist()))['destino'].values[0] <- refactorizar 
                        # print(trip)
                        # print(trip_id_name)
                        table_quote = [[quote['nombre'].values[0], quote['apellido'].values[0], trip_id_name, quote['nro_adultos'].values[0], quote['nro_ninos'].values[0], quote['subtotal'].values[0]]] <- refactorizar 
                        print(tabulate(table_quote, headers=["Nombre", "Apellido", "Viaje a", "Nro. adultos", "Nro. niños", "Subtotal"], tablefmt="pretty"))
        elif menu == 0:
            print("Cerrando programa...")
            db_manager.close_connection()
            sleep(3)
            print("Programa cerrado. ¡Hasta luego!")
            break


if __name__ == "__main__":
    menu()
