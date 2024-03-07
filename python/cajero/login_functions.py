def get_value(type_t: str):
    print(f"""
    Menú de {type_t}
    ----------------------------
    Ingrese el valor:
    """)
    amount = float(input("||==> "))

    if amount > 0:
        return amount
    else:
        print("El monto ingresado no es válido.")
        return False


def get_detail(type_t: str):
    if type_t == "consignación":
        print("""
        Ingrese el detalle de la consignación:
        """)
    elif type_t == "retiro":
        print("""
        Ingrese el detalle del retiro:
        """)

    detail = input("||==> ")

    return detail
