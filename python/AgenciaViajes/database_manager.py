# Librearias para la conexión a la base de datos
import sqlite3
from sqlite3 import Error
# Librería para el manejo de datos
import pandas as pd


class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None # <- Inicializa la conexión a la base de datos al crear el objeto DatabaseManager
        self.create_connection() # <- Llama a la función para crear la conexión a la base de datos 

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file) # <- Crea la conexión a la base de datos
            # Creamos las tablas al iniciar la conexión
            self.create_table_destinations()  # <- Llama a la función para crear la tabla de destinos
            self.create_table_clients()  # <- Llama a la función para crear la tabla de clientes
        except Error as e:
            print(e)

    def close_connection(self):
        if self.conn: # <- Verifica si la conexión existe
            self.conn.close() # <- Cierra la conexión a la base de datos

    # Tabla de destinos #

    def create_table_destinations(self): # <- Función para crear la tabla de destinos
        try:
            # Creamos un cursor para ejecutar sentencias SQL
            cur = self.conn.cursor()

            # Sentencia SQL para crear la tabla de destinos
            sql_create_destinations_table = """
                CREATE TABLE IF NOT EXISTS AgenciaViajes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    destino TEXT NOT NULL UNIQUE,
                    vlr_personaAdulta REAL NOT NULL,
                    vlr_personaMenor REAL NOT NULL
                )
                """
            cur.execute(sql_create_destinations_table) # <- Ejecuta la sentencia SQL para crear la tabla
        except Error as e:
            print(e)

    def insert_data_destinations(self, data): # <- Función para insertar datos en la tabla de destinos
        cur = self.conn.cursor()
        sql = """ INSERT INTO AgenciaViajes(destino, vlr_personaAdulta, vlr_personaMenor)
                  VALUES(?,?,?) """
        cur.execute(sql, data)
        self.conn.commit() # <- Guarda los cambios en la base de datos

    def update_data_destinations(self, data): # <- Función para actualizar los datos de la tabla de destinos
        cur = self.conn.cursor()
        sql = """ UPDATE AgenciaViajes
                  SET destino = ? ,
                      vlr_personaAdulta = ? ,
                      vlr_personaMenor = ?
                  WHERE id = ?"""
        cur.execute(sql, data)
        self.conn.commit()

    def delete_data_destinations(self, id):
        cur = self.conn.cursor()
        sql = "DELETE FROM AgenciaViajes WHERE id = ?"
        cur.execute(sql, (id,))
        self.conn.commit()

    def select_all_data_destinations(self): # <- Función para consultar todos los datos de la tabla de destinos
        # Consulta todos los datos de la tabla de destinos y los guarda en un DataFrame
        df = pd.read_sql_query("SELECT * FROM AgenciaViajes", self.conn) # <- Ejecuta la consulta SQL através de la conexión a la base de datos
        return df # <- Retorna el DataFrame con los datos

    def select_data_destinations(self, id):
        df = pd.read_sql_query(f"SELECT * FROM AgenciaViajes WHERE id = {id}", self.conn)
        return df

    def select_data_destinations_by_name(self, name):
        df = pd.read_sql_query(f"SELECT * FROM AgenciaViajes WHERE destino = '{name}'", self.conn)
        return df

    # Tabla de clientes #

    def create_table_clients(self): # <- Función para crear la tabla de clientes
        try:
            cur = self.conn.cursor()

            sql_create_clients_table = """
                            CREATE TABLE IF NOT EXISTS Personas (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT NOT NULL,
                                apellido TEXT NOT NULL,
                                id_viaje INTEGER,
                                nro_adultos INTEGER NOT NULL,
                                nro_ninos INTEGER NOT NULL,
                                subtotal REAL NOT NULL,
                                FOREIGN KEY (id_viaje) REFERENCES AgenciaViajes(id)
                            )
                        """
            cur.execute(sql_create_clients_table)
        except Error as e:
            print(e)

    def insert_persona_data(self, data):
        cur = self.conn.cursor()
        sql = """ INSERT INTO Personas(nombre, apellido, id_viaje, nro_adultos, nro_ninos, subtotal)
                  VALUES(?, ?, ?, ?, ?, ?) """
        cur.execute(sql, data)
        self.conn.commit()

    def update_persona_data(self, data):
        cur = self.conn.cursor()
        sql = """ UPDATE Personas
                  SET nombre = ? ,
                      apellido = ? ,
                      id_viaje = ? ,
                      nro_adultos = ? ,
                      nro_ninos = ? ,
                      subtotal = ?
                  WHERE id = ?"""
        cur.execute(sql, data)
        self.conn.commit()

    def delete_persona_data(self, id):
        cur = self.conn.cursor()
        sql = "DELETE FROM Personas WHERE id = ?"
        cur.execute(sql, (id,))
        self.conn.commit()

    def select_all_personas_data(self):
        df = pd.read_sql_query("SELECT * FROM Personas", self.conn)
        return df

    def select_persona_data(self, id):
        df = pd.read_sql_query(f"SELECT * FROM Personas WHERE id = {id}", self.conn)
        return df

    def select_personas_data(self, id_viaje):
        df = pd.read_sql_query(f"SELECT * FROM Personas WHERE id_viaje = {id_viaje}", self.conn)
        return df
