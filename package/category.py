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
        Category.lists_urljsons_category.extend(self.list_urljson_category)

    def get_category(self):
        list_urljson_category = []
        for category in Category.data.get("tags"):
            if self.name_category == category.get("name"):
                compteur_pages = 0
                while compteur_pages < 2:
                    urljson = category.get("url") +"/"+ str(compteur_pages) +".json"
                    list_urljson_category.append(urljson)
                    compteur_pages +=1
                return list_urljson_category

if __name__ == "__main__":
    list_cat_all = []
    for cat in LIST_CATEGORY:
        name_cat = Category(cat)
        list_cat_all.extend(name_cat.list_urljson_category)
        print(list_cat_all)