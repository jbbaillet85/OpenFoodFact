# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

from connexionBDD import ConnexionBDD

class Product(ConnexionBDD):
    def __init__(self, food_id, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.food_id = food_id
        query_food_name = f"SELECT food_name FROM food WHERE food_id = {self.food_id}"
        self.food_name = self.get_attribut_product(query_food_name)
        query_category_id = f"SELECT category FROM food WHERE food_id = {self.food_id}"
        self.category_id = self.get_attribut_product(query_category_id)
        query_food_nutriscore = f"SELECT food_nutriscore FROM food WHERE food_id = {self.food_id}"
        self.nutriscore = self.get_attribut_product(query_food_nutriscore)
        query_store_id = f"SELECT store FROM food WHERE food_id = {self.food_id}"
        self.store_id = self.get_attribut_product(query_store_id)
        query_urlOFF = f"SELECT food_urlOFF FROM food WHERE food_id = {self.food_id}"
        self.url = self.get_attribut_product(query_urlOFF)

    def get_attribut_product(self, query):
        self.cursor.execute(query)
        attribut_product = self.cursor.fetchone()
        return attribut_product

if __name__ == "__main__":
    produit = Product(1, "root", "","localhost","eat_well")
    print(produit.nutriscore)