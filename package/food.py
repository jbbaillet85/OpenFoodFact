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
        product_content = []
        for category in self.list_urljson_category:
            category_reponse = requests.get(category)
            category_data = category_reponse.json()
            for product in category_data.get("products"):
                    product_content.append((
                    product.get("product_name"),
                    product.get("nutriscore_grade"),
                    product.get("url"),
                    self.name_category,
                    product.get("stores")))
                    list_food.extend(product_content)
        return list_food

class Food_content:
    def __init__(self, category_name):
        self.food_name = str
        self.food_nutriscore = str
        self.food_urlOFF = str
        self.name_category = category_name
        self.store = str
        self.food_content = [self.food_name, self.food_nutriscore, self.food_urlOFF, self.name_category, self.store]

    def get_food_content(self, url):
        for category in url:
            category_reponse = requests.get(category)
            category_data = category_reponse.json()
            for product in category_data.get("products"):
                self.food_name = product.get("product_name"),
                self.food_nutriscore = product.get("nutriscore_grade"),
                self.food_urlOFF = product.get("url"),
                self.name_category,
                self.store = product.get("stores")




class Food_all:
    def __init__(self):
        self.list_food_all = self.get_list_food_all()
    
    def get_list_food_all(self):
        list_foods_all = []
        for cat in LIST_CATEGORY:
            food = Food(cat)
            foods = food.list_food
            list_foods_all.extend(foods)
        return list_foods_all

if __name__ == "__main__":
    food_all = Food_all()
    print(food_all.list_food_all)
    print(len(food_all.list_food_all))