# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests

from category import *
from dataOFF import *

class Food:
    def __init__(self, name_category):
        self.name_food = str
        self.name_category = name_category
        self.nutriscore = str
        self.name_store = str
        self.url = str
        self.list_urljson_category = self.get_category()
        self.list_food = self.get_food()
    
    def get_category(self):
        return Category(self.name_category).list_urljson_category

    def get_food(self):
        list_food = []
        for category in self.list_urljson_category:
            category_reponse = requests.get(category)
            category_data = category_reponse.json()
            for product in category_data.get("products"):
                    list_food.append(({self.name_category :
                    {"name_food" : product.get("product_name"),
                    "nutriscore" : product.get("nutriscore_grade"),
                    "url" : product.get("url"),
                    "name_category" : product.get("categories"),
                    "name_store" : product.get("stores")}
                    }))
        return list_food


if __name__ == "__main__":
    list_foods_all = []
    for cat in LIST_CATEGORY:
        food = Food(cat)
        foods = food.list_food
        list_foods_all.extend(foods)
    print(list_foods_all)