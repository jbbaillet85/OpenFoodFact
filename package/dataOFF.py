# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


class DataOFF:
    def __init__(self, url, key):
        self.url = url
        self.file_json = self.creat_json()
        self.key = key
        self.value = self.get_value_of_key()
        self.value1 = self.get_value()

    def creat_json(self):
        self.file_json = requests.get(self.url).json()
        return self.file_json

    def get_value_of_key(self):
        for meta_data in self.file_json:
            print(meta_data)
            if meta_data == "products":
                products = []
                for elements in meta_data:
                    if elements == self.key:
                        pass
    
    def get_value(self):
        with open(self.file_json, "r") as file: 
            data = json.load(file) 
            key = data['nutriscore_grade']['categories']['stores']['ingredients_text_fr']['product_name-fr']['url']
            for key, val in data.items():
                print(val)
                data[key][""] = val[""] 



dataoff = DataOFF("https://fr.openfoodfacts.org/categorie/pizzas-royales/1.json", "nutriscore_grade:")
print(dataoff.value1)
