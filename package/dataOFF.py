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
                {"category": product.get("categories")},
                {"nutriscore": product.get("nutriscore_grade")},
                {"url": product.get("url")},
                {"store": product.get("stores")}
            ])
        return list_food


if __name__ == "__main__":
    dataoff = DataOFF("https://fr.openfoodfacts.org/categorie/pizzas-royales/1.json")
    print(dataoff.list_food[0])
