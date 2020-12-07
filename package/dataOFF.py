# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests

class DataOFF:
    """[summary]
    """
    def __init__(self, url):
        self.CRITERIAS = ["categories", "product_name_fr", "nutriscore_grade_fr", "url", "stores"]
        self.url = url
        self.reponse = requests.get(url)
        self.data = self.reponse.json()
        self.list_food = self.get_data()
        self.list_food_for_sql = self.get_data_for_sql()

    def get_data(self):
        list_food = []
        for product in self.data.get("products"):
            list_food.append([
                {"name_food": product.get("product_name_fr")},
                {"nutriscore": product.get("nutriscore_grade")},
                {"url": product.get("url")},
                {"category": product.get("categories")},
                {"store": product.get("stores")}
            ])
        return list_food
    
if __name__ == "__main__":
    pizzas = DataOFF("https://fr.openfoodfacts.org/categorie/pizzas-royales/1.json")
    print(pizzas.list_food_for_sql)