# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

from constants import URL_CATEGORYS, LIST_CATEGORY

class Category:
    reponse = requests.get(URL_CATEGORYS)
    data = reponse.json()
    lists_urljsons_category = []

    def __init__(self, name_category):
        self.name_category = name_category
        self.list_urljson_category = self.get_category()
        Category.lists_urljsons_category.extend(self.list_urljson_category)
    
    def get_category(self):
        list_urljson_category = []
        for category in Category.data.get("tags"):
            if self.name_category == category.get("name"):
                compteur_pages = 0
                while compteur_pages < 4:
                    urljson = category.get("url") +"/"+ str(compteur_pages) +".json"
                    list_urljson_category.append(urljson)
                    compteur_pages +=1
                return list_urljson_category

    def insert_category_table(self):
        pass

if __name__ == "__main__":
    boissons = Category("Boissons")
    
    print(boissons.list_urljson_category)
