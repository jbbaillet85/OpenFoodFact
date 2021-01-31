# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

from BDD.constants import LIST_CATEGORY

from BDD.BDDstore import BDDstoresAll
from BDD.BDDfood import BDDfoodAll


class InsertionBDD:
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
        cursor = self.connexion_db.cursor()
        with open("BDD/creat_tables.sql", "r") as file:
            query = file.read()
            cursor.execute(query, multi=True)
            self.connexion_db.commit()
            cursor.close()

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

    def insert_category(self, list_category):
        """Function inserting the product category names in the Category table

        Args:
            list_category (list): list of category names
        """
        cursor = self.connexion_db.cursor()
        for product in list_category:
            query_select = f"SELECT * FROM Category WHERE category_name = '{product}'"
            cursor.execute(query_select)
            if cursor.rowcount == -1:
                cursor.fetchall()
            if cursor.rowcount == 0:
                query_insert = f"INSERT INTO Category (category_name) VALUES ('{product}')"
                cursor.execute(query_insert)
                self.connexion_db.commit()

    def insert_store(self, list_store):
        """function inserting the blinds in the Store table if they are not already there

        Args:
            list_store (list): list of stores 
        """
        cursor = self.connexion_db.cursor()
        for product in list_store:
            # check if the store is in the database
            query_select = f"SELECT * FROM Store WHERE store_name = '{product}'"
            cursor.execute(query_select)
            if cursor.rowcount == -1:
                cursor.fetchall()
            if cursor.rowcount == 0:
                # insert the store into the base
                query_insert = f"INSERT INTO Store (store_name) VALUES ('{product}')"
                cursor.execute(query_insert)
                self.connexion_db.commit()

    def insert_food(self, list_food):
        """function inserting the products in the Food table if they are not already there

        Args:
            list_food (list): list of food 
        """

        cursor = self.connexion_db.cursor()
        for product in list_food:
            # edit food_name error 'orange'
            food_name = str(product[0])
            food_name = food_name.replace("'", "''")
            # check if food_name is in the database
            query_select = f"SELECT * FROM Food WHERE food_name = '{food_name}'"
            cursor.execute(query_select)
            # if not in bdd -1 or 0
            if cursor.rowcount == -1:
                cursor.fetchall()
            if cursor.rowcount == 0:
                # get the category id
                query_select_cat = f"SELECT category_id from Category WHERE category_name = '{product[3]}'"
                cursor.execute(query_select_cat)
                category_id = cursor.fetchone()
                category_id = category_id[0]
                # get the store id
                id_store = str(product[4])
                id_store = id_store.replace("'", "''")
                query_select_store = f"SELECT store_id from Store WHERE store_name = '{id_store}'"
                cursor.execute(query_select_store)
                store_id = cursor.fetchone()
                store_id = store_id[0]
                # insert data
                query_insert = f"""INSERT INTO Food (food_name, food_nutriscore, food_urlOFF, category, store)
                VALUES ('{food_name}','{product[1]}','{product[2]}','{category_id}','{store_id}')"""
                cursor.execute(query_insert)
                self.connexion_db.commit()
        cursor.close()


if __name__ == "__main__":
    print("""
    --executer le serveur linux: sudo service mysql start
    --executer le serveur windows à partir du dossier mysql/bin: ./mysqld.exe --console
    --arrêter le serveur linux: sudo service mysql stop
    --arrêter le serveur windows: ./mysqladmin.exe -u root -pshutdown
    --executer client mysql linux: sudo mysql -u root -p
    --executer client windows: /mysql.exe -u root -p
    --arrêter le client: exit""")

    mysql1 = InsertionBDD("root", "", "localhost", "eat_well")
    mysql1.create_tables()
    mysql1.purge_tables()
    mysql1.insert_category(LIST_CATEGORY)
    stores_all = BDDstoresAll()
    mysql1.insert_store(stores_all.list_stores_all)
    foods_all = BDDfoodAll()
    mysql1.insert_food(foods_all.list_food_all)
