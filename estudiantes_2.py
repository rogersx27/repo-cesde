import json
students = []


values = {
    1: {"discount": 0.4, "recharge": 0},
    2: {"discount": 0.3, "recharge": 0},
    3: {"discount": 0.1, "recharge": 0},
    4: {"discount": 0, "recharge": 0.1},
    5: {"discount": 0, "recharge": 0.2},
    6: {"discount": 0, "recharge": 0.4}
}

while True:
    print("""
    Menú principal
    ----------------------------
    1. Ingresar estudiante.
    2. Ver estudiantes ingresados.
    3. Salir.
    ----------------------------
    """)

    menu = int(input())

    if menu == 1:
        student = {}
        student_name = input("Ingrese el nombre del estudiante: ")
        tuition_value = float(input("Ingrese el valor de la matrícula: "))
        status = int(input(f"Ingrese el estrato del estudiante {student_name}: "))
        
        if status < 1 or status > 6:
            print("Estrato inválido.")
            continue

        total_discount = (tuition_value * (values[status]["discount"]))
        total_recharge = (tuition_value * (values[status]["recharge"]))
        full_payment = (tuition_value + total_recharge) - total_discount

        student = {
            "nombre": student_name,
            "valor_matricula": tuition_value,
            "estrato": status,
            "descuento": total_discount,
            "recargo": total_recharge,
            "pago_neto": full_payment
        }
        print(f"\nEstudiante {student_name} ingresado exitosamente.\n")
        students.append(student)

    elif menu == 2:
        print("\n")
        print(json.dumps(students, indent=4, sort_keys=False))

    elif menu == 3:
        print("Hasta luego.")
        break
