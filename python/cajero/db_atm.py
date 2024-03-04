import sqlite3
from sqlite3 import Error

import pandas as pd


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
                    email VARCHAR(120) NOT NULL,
                    password VARCHAR(50) NOT NULL,
                    balance REAL DEFAULT  0
                )
            """
            cur.execute(query_users)
        except Error as e:
            print(e)

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

    def select_all_data_user(self):
        df = pd.read_sql_query("SELECT * FROM users", self.conn)
        return df

    def __update_balance_user__(self, id_user: int, amount: float):
        if amount > 0:
            cur = self.conn.cursor()

            round_amount = round(amount, 1)

            sql = f"""
            UPDATE users
            SET balance = balance + {round_amount}
            WHERE id_user = {id_user} """

            cur.execute(sql)
            self.conn.commit()
        else:
            print("El monto debe contener un valor positivo")

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
                date DATE NOT NULL,
                FOREIGN KEY (id_user) REFERENCES users(id_user)
            )
        """

        cur.execute(query_transactions)
        
    def __sql_insert_transaction__(self, data: tuple):
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

    def read_data_transactions(self, id_user: int, details: str, amount: float, type_transaction: str, date: str):
            """
            Lee los datos de una transacción y los procesa según el tipo de transacción.

            Parámetros:
            - id_user (int): ID del usuario.
            - details (str): Detalles de la transacción.
            - amount (float): Monto de la transacción.
            - type_transaction (str): Tipo de transacción ('deposit' o 'withdraw').
            - date (str): Fecha de la transacción.

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
                    
                    data = (id_user, details, amount, type_transaction, date)
                    self.__update_balance_user__(id_user, -amount)
                    self.__sql_insert_transaction__(data)
                        
                elif type_transaction == 'deposit' and amount > 0:
                    data = (id_user, details, amount, type_transaction, date)
                    self.__sql_insert_transaction__(data)
                else:
                    print("El monto debe contener un valor positivo")
                    
            except Error as e:
                print("Error al insertar datos en la tabla de transacciones:", e)
                self.conn.rollback()

    def select_all_data_transactions(self):
        df = pd.read_sql_query("SELECT * FROM transactions", self.conn)
        return df

    def select_all_type_transactions(self, type_transaction):
        df = pd.read_sql_query(
            f"SELECT * FROM transactions WHERE type_transaction = '{type_transaction}'", self.conn)
        return df
