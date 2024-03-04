from db_atm import AtmManager

from functions import clear, get_id_user, get_name_or_last, get_email, get_password

def register_menu():
    """
    Muestra un menú de registro de usuario y solicita al usuario que ingrese la información requerida.
    """
    db_manager = AtmManager()
    
    clear()
    print("""
    Registro de usuario
    ----------------------------
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


def login_menu():
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

    return account, password


def main_menu():
    print("""
    Bienvenido al cajero 24/7
    ----------------------------
    1. Iniciar sesión.
    2. Registrarse.
    0. Salir.
    ----------------------------
    """)

    menu = int(input("||==> "))

    if menu == 1:
        login_menu()
    elif menu == 2:
        register_menu()
    elif menu == 0:
        print("Saliendo del sistema...")
    else:
        print("Opción no valida.")
        login_menu()


def account_menu(name: str, balance: float):
    while True:
        clear()
        print(f"""
        Menú principal
        ----------------------------
        Bienvenido {name} al cajero 24/7
        ----------------------------
        Su saldo es: {balance}
        ----------------------------
        1. Realiza un retiro.
        2. Realiza una consignación.
        3. Consulta tu saldo y movimientos.
        4. Cambia tu clave.
        0. Salir.
        ----------------------------
        """)

        menu = int(input("||==>"))

        if menu == 1:
            pass
        elif menu == 0:
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    
    main_menu()
