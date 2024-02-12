import json

hour_value = 5531
empleados = []

while True:
    print("""
    Menú principal
    ----------------------------
    1. Ingresar empleado.
    2. Ver empleados ingresados.
    3. Salir.
    ----------------------------
    """)

    menu = int(input())

    if menu == 1:
        empleado = {}
        name = input("Ingrese el nombre del empleado: ")
        hijos = int(input(f"Ingrese la cantidad de hijos que el empleado {name} tiene: "))
        hours = int(input(f"Cantidad de horas que el empleado {name} ha trabajado: "))

        if hours >= 47:
            surcharge_value = hour_value + ((35 / 100) * hour_value)
            extra_hours = (hours - 47)
            value_extra_hours = (extra_hours * surcharge_value)
        else:
            extra_hours = 0
            value_extra_hours = 0

        value_hours = (hours * hour_value)

        children_bonus = hour_value * (hijos * 10) if hijos > 3 else hour_value * (hijos * 5)

        total_value_hours = (value_extra_hours + value_hours)

        empleado = {
            "nombre": name,
            "hijos": hijos,
            "valor_hora": hour_value,
            "horas_trabajadas": hours,
            "valor_horas_trabajas": value_hours,
            "hora_extras": extra_hours,
            "valor_extras": round(value_extra_hours, 2),
            "horas_totales_devengadas": total_value_hours,
            "bonificación_hijos": children_bonus,
            "pago_neto": (children_bonus + total_value_hours),
        }

        print(f"\nEmpleado {name} ingresado exitosamente.\n")
        empleados.append(empleado)

    elif menu == 2:
        print("\n")
        print(json.dumps(empleados, indent=4, sort_keys=False))

    elif menu == 3:
        print("Hasta luego.")
        break
