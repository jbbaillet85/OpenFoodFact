# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from category import *

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
                list_store.append(name_store)
        return list_store

class Stores_all:
    def __init__(self):
        self.list_stores_all = self.get_list_stores_all()
    
    def get_list_stores_all(self):
        self.list_stores_all = []
        for cat in LIST_CATEGORY:
            store = Store(cat)
            stores = store.list_stores
            self.list_stores_all.extend(stores)
        return self.list_stores_all

if __name__ == "__main__":
    stores_all = Stores_all()
    print(stores_all.list_stores_all)