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
        except Error as e:
            print(e)

    def create_table(self):
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

    def insert_data(self, data):
        sql = ''' INSERT INTO AgenciaViajes(destino, vlr_personaAdulta, vlr_personaMenor)
                  VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def update_data(self, data):
        sql = ''' UPDATE AgenciaViajes
                  SET destino = ? ,
                      vlr_personaAdulta = ? ,
                      vlr_personaMenor = ?
                  WHERE id = ?'''
        cur = self.conn.cursor()
        cur.execute(sql, data)
        self.conn.commit()

    def delete_data(self, id):
        sql = 'DELETE FROM AgenciaViajes WHERE id = ?'
        cur = self.conn.cursor()
        cur.execute(sql, (id,))
        self.conn.commit()

    def select_all_data(self):
        df = pd.read_sql_query("SELECT * FROM AgenciaViajes", self.conn)
        return df

    def select_data(self, id):
        df = pd.read_sql_query(f"SELECT * FROM AgenciaViajes WHERE id = {id}", self.conn)
        return df

    def close_connection(self):
        if self.conn:
            self.conn.close()
