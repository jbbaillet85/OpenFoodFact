# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from category import *

category = Category()

class Store:
    def __init__(self):
        self.name_store = str
        self.list_category = category.list_urljson_category
        self.list_stores = self.get_store()
    
    def get_store(self):
        list_store = []
        for category in self.list_category:
            category_reponse = requests.get(category)
            category_data = category_reponse.json()
            for store in category_data.get("products"):
                    self.name_store = store.get("stores")
                    list_store.append(self.name_store)
        return set(list_store)

if __name__ == "__main__":
    store = Store()
    print(store.list_stores)