# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests

from category import *

category = Category()

class Food:
    def __init__(self):
        self.id = int
        self.name_food = str
        self.name_category = str
        self.nutriscore = str
        self.name_store = str
        self.url = str
        self.list_category = category.list_urljson_category
        self.list_food = self.get_food()
    
    def get_food(self):
        list_food = []
        for category in self.list_category:
            category_reponse = requests.get(category)
            category_data = category_reponse.json()
            for product in category_data.get("products"):
                    list_food.append(({
                    "name_food" : product.get("product_name"),
                    "nutriscore" : product.get("nutriscore_grade"),
                    "url" : product.get("url"),
                    "name_category" : product.get("categories"),
                    "name_store" : product.get("stores")}))
        return list_food

if __name__ == "__main__":
    pizzaRoyale = Food()
    print(pizzaRoyale.list_category)
    print(pizzaRoyale.list_food[0:3])