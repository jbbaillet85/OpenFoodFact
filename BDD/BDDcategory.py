# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

from BDD.constants import LIST_CATEGORY


class BDDcategory:
    reponse = requests.get("https://fr.openfoodfacts.org/categories.json")
    data = reponse.json()

    def __init__(self, name_category):
        self.name_category = name_category
        self.list_urljson_category = self.get_category()

    def get_category(self):
        list_urljson_category = []
        for category in BDDcategory.data.get("tags"):
            if self.name_category == category.get("name"):
                compteur_pages = 0
                while compteur_pages < 4:
                    urljson = category.get("url") + "/" + str(compteur_pages) + ".json"
                    list_urljson_category.append(urljson)
                    compteur_pages += 1
                return list_urljson_category


class BDDcategory_all:
    def __init__(self):
        self.list_category_name = LIST_CATEGORY
        self.list_categry_url = self.get_list_category_url()

    def get_list_category_url(self):
        list_url = []
        for category in LIST_CATEGORY:
            url = Category(category).list_urljson_category
            list_url.extend(url)
        return list_url


if __name__ == "__main__":
    boissons = BDDcategory("Boissons")
    print(boissons.name_category)
    print(boissons.list_urljson_category)
    cat_all = BDDcategory_all()
    print(cat_all.list_category_name)
    print(cat_all.list_categry_url)
