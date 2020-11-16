# !/usr/bin/env python
# -*- coding: utf-8 -*-

import package.dataOFF


class Food:
    def __init__(self):
        self.id = int
        self.name_food = package.dataOFF
        self.name_category = package.dataOFF
        self.nutriscore = package.dataOFF
        self.name_store = package.dataOFF
        self.url = package.dataOFF

if __name__ == "__main__":
    pizzaRoyale = Food()
    print(pizzaRoyale.url)