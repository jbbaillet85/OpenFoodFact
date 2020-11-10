# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


class DataOFF:
    def __init__(self, url):
        self.url = url
        self.reponse = requests.get(url)
        self.data = self.reponse.json()

    def get_data(self, key):
        for product in self.data.get("products"):
            product.get(key)
            print(product.get(key))


if __name__ == "__main__":
    dataoff = DataOFF("https://fr.openfoodfacts.org/categorie/pizzas-royales/1.json")
    print(dataoff.get_data("stores"))
