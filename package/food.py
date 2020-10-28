# !/usr/bin/env python
# -*- coding: utf-8 -*-

import category
import shop
import nutriscore
import json
import urllib.request


class food:
    def __init__(self):
        self.id = int
        self.name = "product_name_fr"
        self.category = category
        self.ingredients = "ingredients"
        self.nutriscore = nutriscore
        self.shop = shop
        self.url = "url"

    def get_food(self, url):
        self.url = urllib.request.urlopen(url).read()
        return str(self.url.decode('utf-8', 'replace'))
        dict_food = {}
        with open (self.url) as json_data:
            for key, value in json_data.items():
                if key == "product_name_fr":
                    self.name = value
                if key == "ingredients":
                    self.ingredients = value
                if key == "nutriscore_grade":
                    self.nutriscore = value
                if key =="stores":
                    self.shop = value
                if key == "url":
                    self.url = value
                dict_food[key]=value
                json_data.write(dict_food)
            return dict_food

pizzaRoyale = food()
pizzaRoyale.get_food("https://fr.openfoodfacts.org/produit/3270190202974/pizza-cuite-sur-pierre-royale-carrefour.json")
print(pizzaRoyale)
print(pizzaRoyale.name)
print(pizzaRoyale.shop)