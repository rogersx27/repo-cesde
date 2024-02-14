from tabulate import tabulate

from database_manager import DatabaseManager


def menu():
    database = r"./db/AgenciaViajes.db"
    db_manager = DatabaseManager(database)

    while True:
        print("""
        Menú principal
        ----------------------------
        1. Consultar todos los destinos.
        2. Consultar un dato específico.
        3. Insertar un dato.
        4. Actualizar un dato.
        5. Eliminar un dato.
        6. Salir.
        ----------------------------
        """)

        menu = int(input())

        if menu == 1:
            # Consultar todos los datos
            all_data = db_manager.select_all_data()
            destinations = all_data['destino'].values.tolist()  # <- Obtener los destinos

            # Crear una lista de listas con los datos formateados
            table_allData = [[f"{i + 1}", destination] for i, destination in enumerate(destinations)]

            # Imprimir la tabla formateada
            print(tabulate(table_allData, headers=["ID", "Destinos"], tablefmt="pretty"))
        elif menu == 2:
            # Consultar un dato específico
            id = int(input("Ingrese el id del dato que desea consultar: "))
            data = db_manager.select_data(id)  # <- Consultar el dato

            # Crear una lista de listas con los datos formateados
            table_data = [
                [data['destino'].values[0], data['vlr_personaAdulta'].values[0], data['vlr_personaMenor'].values[0]]]
            print(tabulate(table_data, headers=["Destino", "Valor persona adulta", "Valor persona menor"],
                           tablefmt="pretty"))

        elif menu == 3:
        # TODO: Implementar la inserción de un dato

        elif menu == 4:
        # TODO: Implementar la actualización de un dato

        elif menu == 5:
        # TODO: Implementar la eliminación de un dato

        elif menu == 6:
            print("Hasta luego.")
            break


if __name__ == "__main__":
    menu()
