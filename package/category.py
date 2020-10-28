# !/usr/bin/env python
# -*- coding: utf-8 -*-

class category:
    def __init__(self, name):
        self.id = int
        self.name = name
        self.url = "url"

    def get_category(self, url):
        self.url = url
        return self.url+"json"

    def set_category(self):
        pass


pizzasRoyales1 = category("pizzasRoyales1")
pizzasRoyales1.get_category("https://fr.openfoodfacts.org/categorie/pizzas-royales/1")
