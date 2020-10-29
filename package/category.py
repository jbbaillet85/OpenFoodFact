# !/usr/bin/env python
# -*- coding: utf-8 -*-

import food

class category:
    def __init__(self, name):
        self.id = int
        self.name = name
        self.page_url = int
        self.url = f"https://fr.openfoodfacts.org/categorie/{self.name}/{self.page_url}.json"
        self.set_food = set()

    def get_category(self, name, page_url):
        self.name = name
        self.page_url = page_url
        self.url = f"https://fr.openfoodfacts.org/categorie/{self.name}/{self.page_url}.json"
        return self.url

    def set_category(self):
        pass

    def get_set_food(self):
        with "self.url" as category:
            numberFood = 0
            for food in category:
                if food == "products:":
                    food()
                    self.set_food.add(food)
                numberFood +=1
            return self.set_food


pizzas_royales1 = category("pizzas-royales")
pizzas_royales1.get_category("pizzas-royales","1")
pizzas_royales1.get_set_food()
