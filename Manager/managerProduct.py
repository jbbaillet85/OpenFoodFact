# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Manager.connexionBDD import ConnexionBDD


class Product(ConnexionBDD):
    def __init__(self, food_id, user, password, host, database):
        """Class creating product objects from the Food table

        Args:
            food_id (int): product id
            user (str): database username
            password (str): database user password
            host (str): name where the database is hosted
            database (str): database name
        """
        ConnexionBDD.__init__(self, user, password, host, database)
        self.food_id = food_id
        query_food_name = f"SELECT food_name FROM food WHERE food_id = '{self.food_id}'"
        self.food_name = self.get_attribut(query_food_name)
        query_category_id = f"SELECT category FROM food WHERE food_id = '{self.food_id}'"
        self.category_id = self.get_attribut(query_category_id)
        # get category_name
        query_category_name = f"SELECT category_name FROM category WHERE category_id = '{self.category_id}'"
        self.category_name = self.get_attribut(query_category_name)
        query_food_nutriscore = f"SELECT food_nutriscore FROM food WHERE food_id = '{self.food_id}'"
        self.nutriscore = self.get_attribut(query_food_nutriscore)
        query_store_id = f"SELECT store FROM food WHERE food_id = '{self.food_id}'"
        self.store_id = self.get_attribut(query_store_id)
        query_urlOFF = f"SELECT food_urlOFF FROM food WHERE food_id = '{self.food_id}'"
        self.url = self.get_attribut(query_urlOFF)
        # get all the products_id and product_name
        category_id = input("Confirmer la categorie : ")
        query_category_name_products = f"SELECT category_name FROM category WHERE category_id = '{category_id}'"
        self.category_name_products = self.get_attribut(query_category_name_products)
        query_product_all = f"SELECT food_id, food_nutriscore, food_name FROM food WHERE category = '{category_id}'"
        self.product_all = self.get_attribut(query_product_all)
        self.choice_product = self.get_choice_product()

    def print_product(self):
        """display product id and name

        Returns:
            str: product id and name
        """
        return f"#id {self.food_id} : *{self.food_name}*"

    def get_choice_product(self):
        """function retrieving the product id selected by the user

        Returns:
            str: the id selected by the user
        """
        print(f"**{self.category_name_products}**")
        product = f"{self.product_all}".split("),")
        for product_id in product:
            print(product_id)
        choice_product = input(f"Selectionner votre {self.category_name_products}: ")
        while not choice_product.isdigit():
            print("Rentrez un chiffre: ")
            choice_product = input("Rentrer le chiffre du produit: ")
        return choice_product


if __name__ == "__main__":
    produit = Product(1, "root", "", "localhost", "eat_well")
    produit.get_choice_product()
