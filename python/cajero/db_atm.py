# Description: Database connection and operations
import sqlite3
from sqlite3 import Error # <- Nos ayuda a capturar posibles errores en la conexión / operaciones con la base de datos

# Importamos la librería pandas para trabajar con dataframes
import pandas as pd

class AtmManager:
    # Constructor
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.create_connection()
    
    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            # Creamos las tablas al iniciar la conexión
            self.create_table_user()
            self.create_table_transactions()
        except Error as e:
            print(e)
    
    def close_connection(self):
        if self.conn: # <- Verifica si la conexión existe
            self.conn.close()
            
    # Tabla de usuarios #
            
    def create_table_user(self):
        cur = self.conn.cursor()
        
        query_users = """
            CREATE TABLE IF NOT EXISTS users (
                id_user INTEGER PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL,
                email VARCHAR(120) NOT NULL
            )
        """
        cur.execute(query_users)
        
    def insert_data_user(self, data):
        cur = self.conn.cursor()
        sql = """ INSERT INTO users(id_user, name, password, email) 
                  VALUES(?,?,?,?) """
        cur.execute(sql, data)
        self.conn.commit()
        
    def select_all_data_user(self):
        df = pd.read_sql_query("SELECT * FROM users", self.conn)
        return df
        
    # Tabla de transacciones # 
        
    def create_table_transactions(self):
        cur = self.conn.cursor()
        
        query_transactions = """
            CREATE TABLE IF NOT EXISTS transactions (
                id_transaction INTEGER PRIMARY KEY,
                id_user INTEGER,
                details VARCHAR(200),
                amount REAL NOT NULL,
                type_transaction VARCHAR(10) NOT NULL,
                date DATE NOT NULL,
                FOREIGN KEY (id_user) REFERENCES users(id_user)
            )
        """
        
        cur.execute(query_transactions)
        
    def insert_data_transactions(self, data):
        cur = self.conn.cursor()
        sql = """ INSERT INTO transactions(id_user, details, amount, type_transaction, date)
                  VALUES(?,?,?,?,?) """
        cur.execute(sql, data)
        self.conn.commit()
        
    def select_all_data_transactions(self):
        df = pd.read_sql_query("SELECT * FROM transactions", self.conn)
        return df
    
    def select_all_type_transactions(self, type_transaction):
        df = pd.read_sql_query(f"SELECT * FROM transactions WHERE type_transaction = '{type_transaction}'", self.conn)
        return df
