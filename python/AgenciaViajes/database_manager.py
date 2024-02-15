import sqlite3
from sqlite3 import Error

import pandas as pd


class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.create_connection()

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            # Creamos las tablas al iniciar la conexión
            self.create_table_destinations()  # <- Llama a la función para crear la tabla de destinos
            self.create_table_clients()  # <- Llama a la función para crear la tabla de clientes
        except Error as e:
            print(e)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    # Tabla de destinos #

    def create_table_destinations(self):
        try:
            cur = self.conn.cursor()

            sql_create_destinations_table = """
                CREATE TABLE IF NOT EXISTS AgenciaViajes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    destino TEXT NOT NULL UNIQUE,
                    vlr_personaAdulta REAL NOT NULL,
                    vlr_personaMenor REAL NOT NULL
                )
                """
            cur.execute(sql_create_destinations_table)
        except Error as e:
            print(e)

    def insert_data_destinations(self, data):
        sql = ''' INSERT INTO AgenciaViajes(destino, vlr_personaAdulta, vlr_personaMenor)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def update_data_destinations(self, data):
        sql = ''' UPDATE AgenciaViajes
                  SET destino = ? ,
                      vlr_personaAdulta = ? ,
                      vlr_personaMenor = ?
                  WHERE id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def delete_data_destinations(self, id):
        sql = 'DELETE FROM AgenciaViajes WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    def select_all_data_destinations(self):
        df = pd.read_sql_query("SELECT * FROM AgenciaViajes", self.conn)
        return df

    def select_data_destinations(self, id):
        df = pd.read_sql_query(f"SELECT * FROM AgenciaViajes WHERE id = {id}", self.conn)
        return df

    def select_data_destinations_by_name(self, name):
        df = pd.read_sql_query(f"SELECT * FROM AgenciaViajes WHERE destino = '{name}'", self.conn)
        return df

    # Tabla de clientes #

    def create_table_clients(self):
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
        sql = ''' INSERT INTO Personas(nombre, apellido, id_viaje, nro_adultos, nro_ninos, subtotal)
                  VALUES(?, ?, ?, ?, ?, ?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def update_persona_data(self, data):
        sql = ''' UPDATE Personas
                  SET nombre = ? ,
                      apellido = ? ,
                      id_viaje = ? ,
                      nro_adultos = ? ,
                      nro_ninos = ? ,
                      subtotal = ?
                  WHERE id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def delete_persona_data(self, id):
        sql = 'DELETE FROM Personas WHERE id = ?'
        cur = self.conn.cursor()
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
