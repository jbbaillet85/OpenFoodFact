# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

class Product:
    def __init__(self, food_id):
        self.food_id = food_id
        #se connecter à la BDD
        self.connexion_db = self.connect_db("root","","localhost","eat_well")
        #commande sql pour récuperer les éléments composant le produit
        query_food_name = f"SELECT food_name FROM food WHERE food_id = {self.food_id}"
        query_category_id = f"SELECT category_id FROM food WHERE food_id = {self.food_id}"
        query_food_nutriscore = f"SELECT food_nutriscore FROM food WHERE food_id = {self.food_id}"
        query_store_id = f"SELECT store_id FROM food WHERE food_id = {self.food_id}"
        query_urlOFF = f"SELECT food_urlOFF FROM food WHERE food_id = {self.food_id}"
        #attributs du product:
        self.food_name = self.get_food_element(query_food_name)
        self.category_id = self.get_food_element(query_category_id)
        self.nutriscore = self.get_food_element(query_food_nutriscore)
        self.store_id = self.get_food_element(query_store_id)
        self.url = self.get_food_element(query_urlOFF)

    def connect_db(self, user, password, host, database):
        try:
            connexion = mysql.connector.connect(user, password, host, database)
            print("Vous êtes bien connecté")
            return connexion
        except mysql.connector.errors.ProgrammingError:
            print("Vous n'êtes pas connecté")

    def get_food_element(self, query):
        cursor = self.connexion_db.cursor()
        cursor.execute(query)
        cursor.close()
        return cursor.fetchall()

if __name__ == "__main__":
    produit = Product("1")
    print(produit.food_nutriscore)