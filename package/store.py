# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from category import Category, Category_all

from constants import LIST_CATEGORY


class Store:

    def __init__(self, name_category):
        self.name_store = str
        self.name_category = Category(name_category)
        self.list_category = self.name_category.list_urljson_category
        self.list_stores = self.get_store()
    
    def get_store(self):
        list_store = []
        for category in self.list_category:
            category_reponse = requests.get(category)
            category_data = category_reponse.json()
            for store in category_data.get("products"):
                name_store = store.get("stores")
                name_store = str(name_store).replace("'","''")
                list_store.append(name_store)
        return list_store

class Stores_all:
    def __init__(self):
        self.list_stores_all = self.get_list_stores_all()
    
    def get_list_stores_all(self):
        list_stores_all = []
        for cat in LIST_CATEGORY:
            store = Store(cat)
            stores = store.list_stores
            list_stores_all.extend(stores)
        return list_stores_all

if __name__ == "__main__":
    boissons_stores = Store("Boissons")
    print(boissons_stores.name_store)
    print(boissons_stores.list_stores)
    stores_all = Stores_all()
    print(stores_all.list_stores_all)