import sqlite3
from sqlite3 import Error

import pandas as pd

from user_class import User


class AtmManager:
    """
    Crea una instancia de la clase AtmManager, para manejar la base de datos del cajero.
    """
    def __init__(self):
        self.db_file = None
        self.conn = None
        self.create_folder()
        self.create_connection()

    def create_connection(self):
            """
            Crea una conexión a la base de datos y crea las tablas necesarias.

            Returns:
                None
            """
            try:
                self.conn = sqlite3.connect(self.db_file)
                # Creamos las tablas al iniciar la conexión
                self.create_table_user()
                self.create_table_transactions()
            except Error as e:
                print(e)

    def close_connection(self):
            """
            Cierra la conexión con la base de datos.

            Verifica si la conexión existe y la cierra.
            """
            if self.conn:
                self.conn.close()
            
    def create_folder(self):
            """
            Crea una carpeta para almacenar el archivo de base de datos del cajero automático.
            La carpeta se crea en el mismo directorio que el archivo de script actual.
            """
            import os
            db_folder = os.path.join(os.path.dirname(__file__), "data")
            os.makedirs(db_folder, exist_ok=True)
            self.db_file = os.path.join(db_folder, "atm.db")

    # Tabla de usuarios #

    def create_table_user(self):
        try:
            cur = self.conn.cursor()

            query_users = """
                CREATE TABLE IF NOT EXISTS users (
                    id_user INTEGER PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    email VARCHAR(120) NOT NULL UNIQUE,
                    password VARCHAR(50) NOT NULL,
                    balance REAL DEFAULT  0
                )
            """
            cur.execute(query_users)
        except Error as e:
            print(e)

    # Funciones para manejar los usuarios #

    def insert_data_user(self, data) -> None:
            """
            Inserta los datos de un usuario en la base de datos.

            :param data: Una tupla que contiene los datos del usuario en el siguiente orden:
                - (id_user, name, last_name, email, password, balance)

            :return: None
            """
            try:
                cur = self.conn.cursor()
                sql = """ INSERT INTO users(id_user, name, last_name, email, password, balance) 
                    VALUES(?,?,?,?,?,?) """
                    
                cur.execute(sql, data)
                self.conn.commit()
            except Error as e:
                print("Error al insertar datos en la tabla de usuarios:", e)
                self.conn.rollback()

    def login_user(self, email: str, password: int) -> User or None:
            """
            Intenta iniciar sesión con el correo electrónico y la contraseña proporcionados.

            :param email: El correo electrónico del usuario.
            :param password: La contraseña del usuario.
            :return: Una instancia de User si el inicio de sesión es exitoso, None en caso contrario.
            """
            user_data = self.select_user_by_email(email)
            
            if not user_data.empty:
                first_user_data = user_data.iloc[0]
                stored_password = first_user_data.get("password")
                if stored_password == password:
                    list_data = user_data.values.flatten().tolist()
                    return User(AtmManager, *list_data)
                
            return None

    def select_user_by_email(self, email: str):
        df = pd.read_sql_query(f"SELECT * FROM users WHERE email = '{email}'", self.conn)
        return df
    
    def select_user_by_id(self, id_user: int):
        df = pd.read_sql_query("SELECT * FROM users WHERE id_user = ?", self.conn, params=(id_user,))
        return df

    def update_balance_user(self, id_user: int, amount: float):
            """
            Actualiza el saldo de un usuario en la base de datos.

            Parámetros:
            - id_user (int): ID del usuario.
            - amount (float): Monto a sumar al saldo del usuario.

            """
            if amount > 0:
                cur = self.conn.cursor()

                round_amount = round(amount, 1)

                sql = f"""
                UPDATE users
                SET balance = balance + {round_amount}
                WHERE id_user = {id_user} """

                cur.execute(sql)
                self.conn.commit()
            elif amount < 0:
                cur = self.conn.cursor()
                
                round_amount = round(amount, 1)
                
                sql = f"""
                UPDATE users
                SET balance = balance - {round_amount}
                WHERE id_user = {id_user} """
                
                cur.execute(sql)
                self.conn.commit()
            else:
                print("El monto debe contener un valor válido")
        
    # Tabla de transacciones #

    def create_table_transactions(self):
        cur = self.conn.cursor()

        query_transactions = """
            CREATE TABLE IF NOT EXISTS transactions (
                id_transaction INTEGER PRIMARY KEY,
                id_user INTEGER,
                details VARCHAR(250),
                amount REAL NOT NULL,
                type_transaction VARCHAR(10) NOT NULL,
                date VARCHAR(120) NOT NULL,
                FOREIGN KEY (id_user) REFERENCES users(id_user)
            )
        """

        cur.execute(query_transactions)
        
   # Funciones para manejar las transacciones #
   
    def _sql_insert_transaction(self, data: tuple):
        """
        Inserta una transacción en la base de datos.

        Parámetros:
        - data: Una tupla que contiene los datos de la transacción en el siguiente orden:
            (id_user, details, amount, type_transaction, date)
        """
        cur = self.conn.cursor()
        sql = """INSERT INTO transactions(id_user, details, amount, type_transaction, date)
                VALUES(?,?,?,?,?)"""
        cur.execute(sql, data)
        self.conn.commit()

    def read_data_transactions(self, id_user: int, details: str, amount: float, type_transaction: str):
            """
            Lee los datos de una transacción y los procesa según el tipo de transacción.

            Parámetros:
            - id_user (int): ID del usuario.
            - details (str): Detalles de la transacción.
            - amount (float): Monto de la transacción.
            - type_transaction (str): Tipo de transacción ('deposit' o 'withdraw').

            Lanza:
            - ValueError: Si el tipo de transacción no es 'deposit' o 'withdraw'.
            - ValueError: Si el saldo es insuficiente para realizar un retiro.

            """
            if type_transaction not in ["deposit", "withdraw"]:
                raise ValueError("El tipo de transacción debe ser 'consignación' o 'retiro'")

            try:
                balance = pd.read_sql_query("SELECT balance FROM users WHERE id_user = ?", self.conn, params=(id_user,))
                if type_transaction == 'withdraw' and amount > 0:
                    
                    if balance < amount:
                        raise ValueError("No tienes suficiente saldo para realizar el retiro")
                    
                    date = self.get_date()
                    data = (id_user, details, amount, type_transaction, date)
                    self._sql_insert_transaction(data)
                        
                elif type_transaction == 'deposit' and amount > 0:
                    date = self.get_date()
                    data = (id_user, details, amount, type_transaction, date)
                    self._sql_insert_transaction(data)
                    return True
                else:
                    print("El monto debe contener un valor positivo")
                    
            except Error as e:
                print("Error al insertar datos en la tabla de transacciones:", e)
                self.conn.rollback()

    
    def select_all_data_transactions(self):
        df = pd.read_sql_query("SELECT * FROM transactions", self.conn)
        return df

    def select_all_type_transactions_from_user(self, id_user: int, type_transaction: str):
        df = pd.read_sql_query("SELECT * FROM transactions WHERE id_user = ? AND type_transaction = ?", self.conn, params=(id_user, type_transaction))
        return df
    
    def get_date(self):
        from datetime import datetime
        date = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        return date

        
if __name__ == "__main__":
    pass
    