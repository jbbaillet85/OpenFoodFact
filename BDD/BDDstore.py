# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from BDD.BDDcategory import *

from BDD.constants import LIST_CATEGORY


class BDDstore:

    def __init__(self, name_category):
        self.name_category = BDDcategory(name_category)
        self.list_category = self.name_category.list_urljson_category
        self.list_stores = self.get_store()
    
    def get_store(self):
        list_store = []
        for category in self.list_category:
            category_reponse = requests.get(category)
            category_data = category_reponse.json()
            for store in category_data.get("products"):
                if store.get("stores") != None:
                    if store.get("stores") != '':
                        name_store = store.get("stores")
                        name_store = str(name_store).replace("'","''")
                        list_store.append(name_store)
        return list_store

class BDDstoresAll:
    def __init__(self):
        self.list_stores_all = self.get_list_stores_all()
    
    def get_list_stores_all(self):
        list_stores_all = []
        for cat in LIST_CATEGORY:
            store = BDDstore(cat)
            stores = store.list_stores
            list_stores_all.extend(stores)
        return list_stores_all

if __name__ == "__main__":
    #boissons_stores = Store("Boissons")
    #print(boissons_stores.list_stores)
    stores_all = BDDstoresAll()
    print(stores_all.list_stores_all)