# !/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

from Manager.connexionBDD import ConnexionBDD

class Product(ConnexionBDD):
    def __init__(self, food_id, user, password, host, database):
        ConnexionBDD.__init__(self, user, password, host, database)
        self.food_id = food_id
        query_food_name = f"SELECT food_name FROM food WHERE food_id = {self.food_id}"
        self.food_name = self.get_attribut_product(query_food_name)
        query_category_id = f"SELECT category FROM food WHERE food_id = {self.food_id}"
        self.category_id = self.get_attribut_product(query_category_id)
        #recuperer category_name
        query_category_name = f"SELECT category_name FROM category WHERE category_id = '{self.category_id}'"
        self.category_name = self.get_attribut_product(query_category_name)
        query_food_nutriscore = f"SELECT food_nutriscore FROM food WHERE food_id = {self.food_id}"
        self.nutriscore = self.get_attribut_product(query_food_nutriscore)
        query_store_id = f"SELECT store FROM food WHERE food_id = {self.food_id}"
        self.store_id = self.get_attribut_product(query_store_id)
        query_urlOFF = f"SELECT food_urlOFF FROM food WHERE food_id = {self.food_id}"
        self.url = self.get_attribut_product(query_urlOFF)
        #récuperer tous les products_id et product_name
        query_product_all = f"SELECT food_id, food_name FROM food WHERE category = '{self.category_id}'"
        self.product_all = self.get_attribut_product(query_product_all)

        self.choice_product = self.get_choice_product()

    def get_attribut_product(self, query):
        self.cursor.execute(query)
        attribut_product = self.cursor.fetchall()
        attribut_product = str(attribut_product)[1:-1]
        return attribut_product
    
    def print_product(self):
        return f"#id {self.food_id} : *{self.food_name}*"
    
    def get_choice_product(self):
        print(f"**{self.category_name}**")
        product = (f"{self.product_all}".split("),"))
        for product_id in product:
            print(product_id)
        choice_product = input(f"Selectionner votre {self.category_name}: ")
        return choice_product


if __name__ == "__main__":
    produit = Product(1, "root", "","localhost","eat_well")
    produit.get_choice_product()
