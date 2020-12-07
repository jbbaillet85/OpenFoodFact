# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class Category:
    LIST_CATEGORY = ["Boissons", "Desserts", "Epicerie", "Pizzas","Produits laitiers"]
    URL_CATEGORYS = "https://fr.openfoodfacts.org/categories.json"
    reponse = requests.get(URL_CATEGORYS)
    data = reponse.json()

    def __init__(self):
        self.name_category = str
        self.list_urljson_category = self.get_category()
        self.dict_category = {self.name_category : self.list_urljson_category}
        self.list_category = self.get_list_category()
    
    def get_category(self):
        list_urljson_category = []
        for category_selec in Category.LIST_CATEGORY:
            for category in Category.data.get("tags"):
                if category_selec == category.get("name"):
                    self.name_category = category_selec
                    compteur_pages = 0
                    while compteur_pages < 4:
                        urljson = category.get("url") +"/"+ str(compteur_pages) +".json"
                        list_urljson_category.append(urljson)
                        compteur_pages +=1
        return list_urljson_category
    
    def get_list_category(self):
        list_category = []
        i = 0
        for category in Category.LIST_CATEGORY:
            category_dict = {category : self.get_category()}
            list_category.append(category_dict)
            i +=1 
            return list_category
    
    def insert_category_table(self):
        pass

if __name__ == "__main__":
    category = Category()
    #print(category.list_urljson_category)
    print(category.dict_category)
    #print(category.list_category)

