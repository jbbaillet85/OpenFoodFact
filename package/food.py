# !/usr/bin/env python
# -*- coding: utf-8 -*-

import category
import store
import nutriscore
import dataOFF


class Food:
    def __init__(self):
        self.id = int
        self.name = {}
        self.category = category
        self.code_barre = code_barre
        self.ingredients = self.get_ingredients()
        self.nutriscore = nutriscore
        self.store = store
        self.url = f"https://fr.openfoodfacts.org/api/v0/product/{self.code_barre}.json"
        self.file_json = dataOFF


pizzaRoyale = food("3270190202974")
# pizzaRoyale.get_food()
# print(pizzaRoyale)
# print(pizzaRoyale.name)
# print(pizzaRoyale.shop)
print(pizzaRoyale.ingredients)
