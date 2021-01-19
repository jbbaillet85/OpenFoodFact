# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

from constants import LIST_CATEGORY

from BDDstore import BDDstoresAll
from BDDfood import BDDfoodAll

class InsertionBDD:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connexion_db = self.connect_db()
        self.cursor = self.connexion_db.cursor()

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
        cursor = self.connexion_db.cursor()
        with open("creat_tables.sql", "r") as file:
            query = file.read()
            cursor.execute(query, multi=True)
            self.connexion_db.commit()
            cursor.close()
    
    def purge_tables(self):
        list_tables = ["Substitute","Food","Category", "Store"]
        for table in list_tables:
            cursor = self.connexion_db.cursor()
            #suprimer les contraintes puis les recréer
            query_delete_contraintes = f"SET FOREIGN_KEY_CHECKS = 0"
            query_delete = f"TRUNCATE TABLE {table}"
            query_create_contraintes = f"SET FOREIGN_KEY_CHECKS = 1"
            cursor.execute(query_delete_contraintes)
            cursor.execute(query_delete)
            cursor.execute(query_create_contraintes)
            self.connexion_db.commit()
            cursor.close()
    
    def insert_category(self, list_category):
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
        cursor = self.connexion_db.cursor()
        for product in list_store:
            #verifie si le store est dans la base
            query_select = f"SELECT * FROM Store WHERE store_name = '{product}'"
            cursor.execute(query_select)
            if cursor.rowcount == -1:
                cursor.fetchall()
            if cursor.rowcount == 0:
                #inserer le store dans la base
                query_insert = f"INSERT INTO Store (store_name) VALUES ('{product}')"
                cursor.execute(query_insert)
                self.connexion_db.commit()
    
    def insert_food(self, list_food):
        cursor = self.connexion_db.cursor()
        for product in list_food:
            #modifier food_name erreure 'orange''
            food_name = str(product[0])
            food_name = food_name.replace("'","''")
            #verifie si food_name est dans la base
            query_select = f"SELECT * FROM Food WHERE food_name = '{food_name}'"
            cursor.execute(query_select)
            # si pas dans bdd -1 ou 0
            if cursor.rowcount == -1:
                cursor.fetchall()
            if cursor.rowcount == 0:
                #récuperer l'id de category
                query_select_cat = f"SELECT category_id from Category WHERE category_name = '{product[3]}'"
                cursor.execute(query_select_cat)
                category_id = cursor.fetchone()
                category_id = category_id[0]
                #récupérer l'id de store
                id_store = str(product[4])
                id_store = id_store.replace("'","''")
                query_select_store = f"SELECT store_id from Store WHERE store_name = '{id_store}'"
                cursor.execute(query_select_store)
                store_id = cursor.fetchone()
                store_id = store_id[0]
                # inserer les données
                query_insert = f"""INSERT INTO Food (food_name, food_nutriscore, food_urlOFF, category, store)
                VALUES ('{food_name}','{product[1]}','{product[2]}','{category_id}','{store_id}')"""
                cursor.execute(query_insert)
                self.connexion_db.commit()
                print(product)
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