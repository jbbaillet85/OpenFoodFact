# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class dataOFF:
    def __init__(self, url):
        self.name = "name"
        self.data = requests.get(url)


    def encoding(self):
        self.encoding = 'utf-8'
        self.j


dataoff = dataOFF('https://fr.openfoodfacts.org/categorie/popcorn/1.json')
dataoff.json
print(dataoff)
