from tabulate import tabulate

from user_class import User

from register_functions import clear, get_id_user, get_name_or_last, get_email, get_password


def register_menu():
    """
    Muestra un menú de registro de usuario y solicita al usuario que ingrese la información requerida.
    """
    from db_atm import AtmManager
    db_manager = AtmManager()
    
    clear()
    print("""
    Registro de usuario / Presione 0 para volver al menú principal
    --------------------------------------------------------------
    Ingrese su identificación ciudadana:
    """)

    id_user = get_id_user()

    name = get_name_or_last("nombre")

    last_name = get_name_or_last("apellido")

    email = get_email()

    password = get_password()
    
    data = (id_user, name, last_name, email, password, 0)
    db_manager.insert_data_user(data)
    db_manager.close_connection()
    
    print("Usuario registrado con éxito. Ya puede iniciar sesión.")
    return True

def login_menu():
    from db_atm import AtmManager
    db_manager = AtmManager()
    
    clear()
    print("""
    Iniciar sesión
    ----------------------------
    Ingrese su correo electrónico.
    """)

    email = input("||==> ")

    print("""
    Ingrese su clave.
    """)

    password = input("||==> ")
    
    user_active = db_manager.login_user(email, password)
    if user_active:
        account_menu(user_active)
    else:
        print("Correo electrónico o contraseña incorrectos.")

    db_manager.close_connection()
    return True


def atm_app():
    print("""
    Bienvenido al cajero 24/7
    ----------------------------
    1. Iniciar sesión.
    2. Registrarse.
    0. Salir.
    ----------------------------
    """)
    try:
        menu = int(input("||==> "))

        if menu == 1:
            if login_menu():
                clear()
                return True
        elif menu == 2:
            if register_menu():
                clear()
                return True
        elif menu == 0:
            print("Saliendo del sistema...")
            return False
        else:
            print("Opción no valida.")
            return True
    except ValueError:
        print("Debe ingresar un número de la lista.")
        return True


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

def account_menu(user: User):
    while True:
        clear()
        print(f"""
        Menú principal
        ----------------------------
        Bienvenido {user.name} al cajero 24/7
        ----------------------------
        Su saldo es: {user.balance}
        ----------------------------
        1. Realiza un retiro.
        2. Realiza una consignación.
        3. Consulta tus movimientos.
        4. Cambia tu clave.
        0. Salir.
        ----------------------------
        """)

        menu = int(input("||==>"))

        if menu == 1:
            amount = get_value("retiros")
            detail = get_detail("retiro")
            user.do_withdraw(amount, detail)
        elif menu == 2:
            amount = get_value("consignaciones")
            detail = get_detail("consignación")
            user.do_deposit(amount, detail)
        elif menu == 3:
            data = user.consult_deposits()
            print(tabulate(data, headers=["Detalles", "Monto", "Fecha"], tablefmt="pretty"))
            exit_menu = input("Presione enter para continuar...")
        elif menu == 4:
            pass
        elif menu == 0:
            print("Saliendo de la cuenta...")
            break


if __name__ == "__main__":
    cycle = True
    while cycle == True:
        do_app = atm_app()
        if do_app == False:
            cycle = False
