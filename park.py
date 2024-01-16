#| ------------------------------------------------------------------------------------------------------------------------------- |#
#? Importación de librerias

import random
from datetime import datetime

#| ------------------------------------------------------------------------------------------------------------------------------- |#
#? Definición de variables


print("-----BIENVENIDO AL SISTEMA DE PARQUEADEROS JMG")

#Definir cuantos cupos tiene el parqueadero en motos y carros
camp_cars = int(input("Digite el número total de espacios para carro: "))
camp_moto = int(input("Digite el número total de espacios para moto: "))

#Definir los campos del parqueadero
list_camp_cars = []
list_camp_moto = []

#Crear listas para definir a los vehiculos
register_car = []
register_moto = []

#Definir la tarifa de cobro por tiempo
cost_hour_car = 3500
cost_hour_moto = 2000

#| ------------------------------------------------------------------------------------------------------------------------------- |#
#? Definición de funciones

#Mientras la lista de campos sea menor o igual campos, permitame ingresar una identificacion del campo
while int(len(list_camp_cars)) < camp_cars:
    list_camp_cars.append(
        {"place": input("Ingrese la identificación del lugar a asignar para carro : "), "avalible": True})

while int(len(list_camp_moto)) < camp_moto:
    list_camp_moto.append(
        {"place": input("Ingrese la identificación del lugar a asignar para moto : "), "avalible": True})

#| ------------------------------------------------------------------------------------------------------------------------------- |#

def print_cars():
    for campo in list_camp_cars:
        if campo["avalible"] == True:
            print(f'Los campos disponibles para carros son: {campo["place"]} ')
        else:
            print("Lo sentimos, todos los campos se encuentran ocupados")
            
#| ------------------------------------------------------------------------------------------------------------------------------- |#

def print_moto():
    for campo in list_camp_moto:
        if campo["avalible"] == True:
            print(f'Los campos disponibles para motos son: {campo["place"]} ')
        else:
            print("Lo sentimos, todos los campos se encuentran ocupados")
            
#| ------------------------------------------------------------------------------------------------------------------------------- |#

#  función para ingresar vehículos
def enter_vehicle():
    # variable para seleccionar vehículo
    type_vehicle = int(input(
    """Digite el tipo de vehiculo
    1. Carros
    2. Motos
    """))

    # añadir un carro
    if type_vehicle == 1:
        # obtener placa
        plate = str(input("Digite la placa del vehiculo: "))
        # obtener hora de entrada
        hour_start_car = datetime.now().strftime('%H:%M')
        # le asignamos aleatoriamente un espacio al vehículo de la lista de espacios disponibles
        assing_place = random.choice(list_camp_cars)
        # añadimos el vehíuclo registrado a la lista de "register_car"
        register_car.append(
            {"placa":plate, "espacio_asignado": assing_place["place"], "hora_entrada_carro": hour_start_car}
        )
        # recorremos la lista de campos disponibles para carros
        for campo in list_camp_cars:
            # buscamos el key "place" de la lista de campos disponibles y lo comparamos con el espacio asignado aleatoriamente
            if campo["place"] == assing_place["place"]:
                # cambiamos el estado de la key "avalible" por false, debido a que ese espacio ya no está disponible
                campo["avalible"] = False
                print(f'El vehiculo con placa {plate} se encuentra en el espacio {assing_place["place"]} e ingresó a la hora {hour_start_car}')
                # retornamos "true" para que el bucle prosiga
                return True

    elif type_vehicle == 2:
        plate = str(input("Digite la placa del vehiculo: "))
        hour_start_moto = datetime.now().strftime('%H:%M')
        assing_place = random.choice(list_camp_moto)
        register_moto.append({"placa": plate, "espacio_asignado": assing_place["place"], "hora_entrada_moto": hour_start_moto})
        for campo in list_camp_moto:
            if campo["place"] == assing_place["place"]:
                campo["avalible"] = False
                print(f'El vehiculo con placa {plate} se encuentra en el espacio {assing_place["place"]} e ingresó a la hora {hour_start_moto}')
                return True

    else:
        print("Opción invalida")
        return False
    
#| ------------------------------------------------------------------------------------------------------------------------------- |#

# función para realizar la salida de un vehículo
def exit_vehicle():
    # obtener placa
    type_vehicle = int(input("""Digite el tipo de vehículo para dar salida:
     1. Carro
     2. Moto
     """))

    if type_vehicle == 1:
        # obtenemos el vehículo que queremos retirar
        plate_pay_car = str(input("Digite la placa del vehiculo: "))
        # recorremos la lista de carros registrados
        for camp in register_car:
            # evaluamos el key "placa" de lista de carros registrados y lo comparamos con la placa ingresa en el input de la variable "plate_pay_car"
            if camp["placa"] == plate_pay_car:
                print("Placa válida")
                # obtenemos la hora de salida
                exit_hour_car = datetime.now().strftime('%H:%M')
                # añadimos un registro de hora de salida a la lista de campos registrados
                register_car.append({"hora salida carro": exit_hour_car})
                # evaluamos el tiempo total que estuvo el carro en el parqueadero
                total_time= datetime.strptime(exit_hour_car, '%H:%M') - datetime.strptime(camp['hora_entrada_carro'], '%H:%M')
                # añamos el valor a pagar
                cost_total_car = (total_time.seconds / 3600) * cost_hour_car
                # recorremos la lista de campos disponibles para carros
                for camp in list_camp_cars:
                    # ubicamos el key "avalible" para reestablecer su valor a "true" ya que el campo queda disponible
                    camp["avalible"] = True
                return print(f'La placa {plate_pay_car} con hora de salida {exit_hour_car} deberá pagar un total de {cost_total_car}')

            else:
                return  print("Ingrese una placa válida")

    if type_vehicle == 2:
        plate_pay_moto = str(input("Digite la placa del vehiculo: "))
        for camp in register_moto:
            if camp["placa"] == plate_pay_moto:
                print("Placa válida")
                exit_hour_moto = datetime.now().strftime('%H:%M')
                register_moto.append({"hora salida moto": exit_hour_moto})
                total_time= datetime.strptime(exit_hour_moto, '%H:%M') - datetime.strptime(camp['hora_entrada_moto'], '%H:%M')
                cost_total_moto = (total_time.seconds / 3600) * cost_hour_moto
                for camp in list_camp_moto:
                    camp["avalible"] = True
                return print(f'La placa {plate_pay_moto} con hora de salida {exit_hour_moto} deberá pagar un total de {cost_total_moto}')

            else:
                return  print("Ingrese una placa válida")
#| ------------------------------------------------------------------------------------------------------------------------------- |#
#Creación del menu para brindar opciones al usuario de lo que puede realizar

def menu_principal():
    while True:
        menu = int(input("""Digite una de las siguientes opciones:
        1. Consultar espacios disponibles
        2. Ingresar el vehículo
        3. Registrar salida de vehículo
        4. Imprimir vehiculos
        5. Salir 
        """))
        if menu == 1:
            print_cars()
            print_moto()

        elif menu == 2:
            if enter_vehicle():
                print("Ingreso de vehiculo exitoso. Volviendo al menú principal")
            else:
                print("Error al ingresar el vehículo")

        elif menu == 3:
            exit_vehicle()

        elif menu == 4:
            print(f"""Las motos registradas son:
            {register_moto} 
            
            """)
            print(f"""Los carros registrados son:
            {register_car} 
            
            """)


        elif menu == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida")
            
#| ------------------------------------------------------------------------------------------------------------------------------- |#
#? Ejecución del programa

if __name__ == '__main__':
    menu_principal()