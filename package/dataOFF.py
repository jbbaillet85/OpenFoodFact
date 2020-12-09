# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests

from constants import CRITERIAS

class DataOFF:
    """[summary]
    """
    def __init__(self, url):
        self.url = url
        self.reponse = requests.get(url)
        self.data = self.reponse.json()
        self.list_food = self.get_data()

    def get_data(self):
        list_food = []
        for product in self.data.get("products"):
            food = []
            for critere in CRITERIAS:
                food.append({critere : product.get(critere)})
            list_food.append(food)
        return list_food
    
if __name__ == "__main__":
    pizzas = DataOFF("https://fr.openfoodfacts.org/categorie/pizzas-royales/1.json")
    print(pizzas.list_food)