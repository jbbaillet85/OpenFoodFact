# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

import dataOFF


class InsertionBDD:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connexion_db = self.connect_db()

    def connect_db(self):
        try:
            connexion = mysql.connector.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                database = self.database)
            print("Vous êtes bien connecté")
            return connexion
        except mysql.connector.errors.ProgrammingError:
            print("Vous n'êtes pas connecté")
    
    def create_tables(self):
        connexion = self.connect_db()
        cursor = connexion.cursor()
        with open("create_tables.sql", "r") as file:
            query = file.read()
        cursor.execute(query)
        connexion.commit()
        cursor.close()
    
    def insert_data(self, list_data):
        for product in list_data:
            query_select = f"SELECT * FROM Categories WHERE category_name = {product}"
            query_insert = f"INSERT INTO Category (name_category) VALUES ({product})"
            cursor.execute(query_select)
            cursor.execute(query_insert)
            connexion.commit()

if __name__ == "__main__":
    print("""
    --executer le serveur linux: sudo service mysql start
    --executer le serveur windows à partir du dossier mysql/bin: ./mysqld.exe --console
    --arrêter le serveur linux: sudo service mysql stop
    --arrêter le serveur windows: ./mysqladmin.exe -u root -pshutdown
    --executer client mysql linux: sudo mysql -u root -p
    --executer client windows: /mysql.exe -u root -p
    --arrêter le client: exit""")
    
    mysql1 = InsertionBDD("root", "iotabeta85", "localhost", "eat_well")
    mysql1.connect_db()
        