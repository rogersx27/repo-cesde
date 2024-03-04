from os import system, name
from time import sleep

def clear():
    """
    La función clear() se encarga de limpiar la pantalla del terminal.
    Cuenta con una condición que verifica si el sistema operativo es Windows o Linux:
        ° En caso de ser Windows, se ejecuta el comando "cls" que limpia la pantalla.
        ° En caso de ser Linux, se ejecuta el comando "clear" que limpia la pantalla.
    Contiene el método sleep() que se encarga de hacer una pausa de 1 segundo para que el usuario pueda leer el mensaje que se muestra en pantalla.
    """
    
    sleep(1)
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def has_numbers(inputString: str) -> bool:
    """ 
    Verifica si una cadena de texto contiene números.

    :param inputString: La cadena de texto que se va a verificar.
    :arg type: str
    :return:
        - True si la cadena de texto contiene números, False de lo contrario.
    """
    return any(char.isdigit() for char in inputString)


def has_special_characters(inputString: str) -> bool:
    """
    Verifica si una cadena de texto contiene caracteres especiales.

    :param inputString: La cadena de texto que se va a verificar.
    :arg type: str
    :return: 
        - True si la cadena de texto contiene caracteres especiales, False en caso contrario.
    """
    import string
    return any(char in string.punctuation for char in inputString)


def validate_password(password: int) -> bool:
    """
    Verifica si la clave ingresada es igual a la clave confirmada.

    :param password: La clave ingresada por el usuario.
    :type password: int
    :raises ValueError: Si el usuario no ingresa un número al confirmar la clave.
    :return: True si la clave es válida, False en caso contrario.
    :rtype: bool
    """
    try:
        print("""
        Confirme su clave.
        """)

        _ = int(input("||==> "))

        if _ != password:
            return False
        else:
            return True
    except ValueError:
        print("Para confirmar su clave, debe ingresar un número.")


def get_id_user() -> int:
    """
    Solicita al usuario que ingrese su identificación ciudadana.
    
    :raises ValueError: Si el usuario ingresa un valor no numérico.
    :return: int La identificación ciudadana ingresada por el usuario.
    
    """
    while True:
        try:
            id_user = int(input("||==> "))
            if id_user <= 0:
                print("Su identificación debe ser un número positivo mayor que cero.")

            elif len(str(id_user)) < 8:
                print("Su identificación debe tener al menos 8 dígitos.")

            elif len(str(id_user)) > 10:
                print("Su identificación no debe tener más de 10 dígitos.")

            else:
                return id_user
        except ValueError: # <- Captura la excepción ValueError en caso de que el usuario ingrese un valor no numérico
            print("Su identificación debe ser un número.")
            continue


def get_name_or_last(type: str) -> str:
    """
    Solicita al usuario que se ingrese un nombre o apellido según el tipo que se le pase como argumento.
    Retorna el nombre o apellido ingresado por el usuario.

    :param type: El tipo de dato que se solicita al usuario (nombre o apellido).

    :return: 
        - str El nombre o apellido ingresado por el usuario.
    """
    while True:
        clear()
        print(f"""
        Ingrese su {type}:
        """)
        response = str(input("||==> "))
        if len(name) <= 1:
            print(f"Ingrese un {type} válido.")

        elif has_numbers(response): # <- Llama a la función has_numbers
            print(f"Ingrese un {type} válido.")

        elif has_special_characters(response): # <- Llama a la función has_special_characters 
            print(f"Ingrese un {type} válido.")

        else:
            return response


def get_email() -> str:
    """
    Obtiene el correo electrónico ingresado por el usuario.

    Utiliza el módulo re para validar el correo electrónico ingresado.
    El correo electrónico debe cumplir con el siguiente patrón:
    - Debe contener letras, números, guiones bajos, puntos y signos más o menos.
    - Debe tener un único símbolo @.
    - Después del símbolo @, debe haber letras, números y guiones.
    - Después del último guion, debe haber letras, números y guiones.

    Si el correo electrónico ingresado no cumple con el patrón, se solicitará al usuario que ingrese un correo electrónico válido.

    :return: str El correo electrónico ingresado por el usuario.
    """
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        clear()
        print("""
        Ingrese su correo electrónico:
        """)
        email = str(input("||==> "))
        # Verifica si el correo electrónico ingresado cumple con el patrón
        if re.match(pattern, email) is None:
            print("Ingrese un correo electrónico válido.")
        else:
            return email


def get_password() -> int:
    """
    Solicita al usuario que ingrese su clave y la valida.

    :raises ValueError: Si el usuario no ingresa un número al confirmar la clave.
    :return: 
        - int La clave ingresada por el usuario.

    """
    while True:
        try:
            clear()
            print("""
        -----------------------------------------------------------
        | Su clave debe contener 4 dígitos y no debe tener letras |
        -----------------------------------------------------------
        Ingrese su clave: 
            """)

            password = int(input("||==> "))

            if len(str(password)) != 4:
                print("Su clave debe ser un número de 4 dígitos.")
                continue
            
            if validate_password(password) == False:
                print("Las claves no coinciden. Vuelva a intentarlo.")
                continue

            return password

        except ValueError:
            print("Su clave debe ser un número.")
            continue

