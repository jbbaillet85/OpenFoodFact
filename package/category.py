# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

from constants import URL_CATEGORYS, LIST_CATEGORY

class Category:
    reponse = requests.get(URL_CATEGORYS)
    data = reponse.json()
    lists_urljsons_category = []
    list_names_category = []

    def __init__(self, name_category):
        self.name_category = name_category
        self.list_urljson_category = self.get_category()
        self.set_name_category = self.get_category_of_category()
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
    
    def get_category_of_category(self):
        list_name_category = []
        for urljson in self.list_urljson_category:
            urljson_reponse = requests.get(urljson)
            urljson_json = urljson_reponse.json()
            for product in urljson_json.get("products"):
                categorys = product.get("categories")
                categorys = categorys.split(",")
                list_name_category.extend(categorys)
        return set(list_name_category)

    def insert_category_table(self):
        for name_category in self.set_name_category:
            query_insert = f"INSERT INTO category(category_name) VALUES {name_category}"

if __name__ == "__main__":
    #boissons = Category("Boissons")
    #print(boissons.list_urljson_category)
    #print(boissons.set_name_category)
    list_cat_all = []
    for cat in LIST_CATEGORY:
        name_cat = Category(cat)
        list_name = name_cat.set_name_category
        list_cat_all.extend(list_name)
        print(list_cat_all)

 