# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


class DataOFF:
    def __init__(self, url):
        self.url = url
        self.reponse = requests.get(url)
        self.data = self.reponse.json()
        self.list_food = self.get_data()

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
    for data in pizzas.list_food:
        print(data)
