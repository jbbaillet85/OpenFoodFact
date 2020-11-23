# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class Category:
    def __init__(self):
        self.LIST_CATEGORY = ["Boissons", "Desserts", "Epicerie", "Pizzas","Produits laitiers"]
        self.url = "https://fr.openfoodfacts.org/categories.json"
        self.list_name_category = []
        self.list_urljson_category = []
        self.reponse = requests.get(self.url)
        self.data = self.reponse.json()
        self.list_category = self.get_category()
    
    def get_category(self):
        self.list_category = []
        for category_selec in self.LIST_CATEGORY:
            for category in self.data.get("tags"):
                if category_selec == category.get("name"):
                    self.list_category.append([
                        category.get("name"),
                        category.get("url")])
                    self.list_name_category.append(category.get("name"))
                    compteur_pages = 0
                    while compteur_pages < 4:
                        urljson = category.get("url") +"/"+ str(compteur_pages) +".json"
                        self.list_urljson_category.append(urljson)
                        compteur_pages +=1
        return self.list_category
    
    def insert_category_table(self):
        pass

if __name__ == "__main__":
    category = Category()
    print(category.list_category)
    print(category.list_urljson_category)
    print(category.list_name_category)
