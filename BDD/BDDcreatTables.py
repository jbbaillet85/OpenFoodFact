# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector


class CreatTables:
    def __init__(self, user, password, host, database):
        """class inserting in the mysql database the data: categorys, stores, and foods

        Args:
            user (str): database username
            password (str): database user password
            host (str): name where the database is hosted
            database (str): database name
        """
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connexion_db = self.connect_db()
        self.cursor = self.connexion_db.cursor()

    def connect_db(self):
        """function to connect to the server

        Returns:
            MySQLConnection: Connection to the server
        """
        try:
            connexion = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database)
            print("Vous êtes bien connecté")
            return connexion
        except mysql.connector.errors.ProgrammingError:
            print("Vous n'êtes pas connecté")

    def create_tables(self):
        """function creating the database tables
        """
        table_category = """CREATE TABLE IF NOT EXISTS Category (
        category_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        category_name VARCHAR(60) NOT NULL)
        ENGINE = InnoDB;"""
        table_store = """CREATE TABLE IF NOT EXISTS Store(
        store_id SMALLINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        store_name VARCHAR(255) NOT NULL)
        ENGINE = InnoDB;"""
        table_food = """CREATE TABLE IF NOT EXISTS Food(
        food_id SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        food_name VARCHAR(255) NOT NULL,
        food_nutriscore VARCHAR(1) NOT NULL,
        food_urlOFF VARCHAR(255) NOT NULL,
        category SMALLINT NOT NULL,
        store SMALLINT,
        CONSTRAINT fk_category_id FOREIGN KEY (category) REFERENCES Category(category_id),
        CONSTRAINT fk_store_id FOREIGN KEY (store) REFERENCES Store(store_id))
        ENGINE=InnoDB;"""
        table_substitute = """CREATE TABLE IF NOT EXISTS Substitute(
        id_substitute SMALLINT,
        id_substited SMALLINT,
        CONSTRAINT fk_substitute FOREIGN KEY(id_substitute) REFERENCES Food(food_id),
        CONSTRAINT fk_substituted FOREIGN KEY(id_substited) REFERENCES Food(food_id))
        ENGINE=InnoDB;"""
        cursor = self.connexion_db.cursor()
        cursor.execute(f"USE {self.database};")
        cursor.execute(table_category)
        cursor.execute(table_store)
        cursor.execute(table_food)
        cursor.execute(table_substitute)
        print("Création des tables terminé")

    def purge_tables(self):
        """function purging data from tables
        """
        list_tables = ["Substitute", "Food", "Category", "Store"]
        for table in list_tables:
            cursor = self.connexion_db.cursor()
            # remove the constraints then recreate them
            query_delete_contraintes = "SET FOREIGN_KEY_CHECKS = 0"
            query_delete = f"TRUNCATE TABLE {table}"
            query_create_contraintes = "SET FOREIGN_KEY_CHECKS = 1"
            cursor.execute(query_delete_contraintes)
            cursor.execute(query_delete)
            cursor.execute(query_create_contraintes)
            self.connexion_db.commit()
            cursor.close()
